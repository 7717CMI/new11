'use client'

import { useEffect, useState } from 'react'
import { loadCustomerData, applyFilters, getUniqueValues, FilterState } from '@/lib/utils'
import { Customer } from '@/lib/types'
import { Filters } from '@/components/filters'
import { BarChart, PieChart, GroupedBarChart } from '@/components/charts'
import { COLORS } from '@/lib/types'
import { DemoDataNotice } from '@/components/demo-notice'

export default function AnalyticsPage() {
  const [customers, setCustomers] = useState<Customer[]>([])
  const [filteredCustomers, setFilteredCustomers] = useState<Customer[]>([])
  const [filters, setFilters] = useState<FilterState>({
    industries: [],
    clouds: [],
    regions: [],
    optTypes: [],
    licenses: [],
    optRange: [0, 50],
  })
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    loadCustomerData().then((data) => {
      setCustomers(data)
      setFilteredCustomers(data)
      setLoading(false)
    })
  }, [])

  useEffect(() => {
    const filtered = applyFilters(customers, filters)
    setFilteredCustomers(filtered)
  }, [customers, filters])

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="text-lg text-gray-600">Loading...</div>
      </div>
    )
  }

  const uniqueValues = getUniqueValues(customers)

  // License ecosystem breakdown
  const licenseCounts: Record<string, number> = {}
  filteredCustomers.forEach(c => {
    c.License_Ecosystem.split(',').forEach(lic => {
      const trimmed = lic.trim()
      if (trimmed) {
        licenseCounts[trimmed] = (licenseCounts[trimmed] || 0) + 1
      }
    })
  })
  const licenseData = Object.entries(licenseCounts)
    .map(([License, Count]) => ({ License, Count }))
    .sort((a, b) => b.Count - a.Count)

  // Regional analysis
  const regionData: Record<string, { cloud: number[], elo: number[], total: number[] }> = {}
  filteredCustomers.forEach(c => {
    const match = c.Geographical_Presence.match(/operates across (.+)$/i)
    const region = match ? match[1].trim() : 'Unknown'
    if (!regionData[region]) {
      regionData[region] = { cloud: [], elo: [], total: [] }
    }
    regionData[region].cloud.push(c.Cloud_Optimization_Potential)
    regionData[region].elo.push(c.ELO_Optimization_Potential)
    regionData[region].total.push(c.Total_Optimization_Potential)
  })
  const regionSummary = Object.entries(regionData).map(([Region, values]) => ({
    Region,
    'Avg Cloud %': values.cloud.reduce((a, b) => a + b, 0) / values.cloud.length,
    'Avg ELO %': values.elo.reduce((a, b) => a + b, 0) / values.elo.length,
  })).slice(0, 10)

  // Decision maker distribution
  const decisionMakerCounts: Record<string, number> = {}
  filteredCustomers.forEach(c => {
    decisionMakerCounts[c.Decision_Maker] = (decisionMakerCounts[c.Decision_Maker] || 0) + 1
  })
  const decisionMakerData = Object.entries(decisionMakerCounts)
    .map(([Role, Count]) => ({ Role, Count }))
    .sort((a, b) => b.Count - a.Count)

  return (
    <div className="max-w-7xl mx-auto page-container">
      <div className="mb-6">
        <h2 className="text-2xl font-bold text-gray-800 mb-1">Analytics Deep-Dive</h2>
        <p className="text-gray-600">Advanced analysis and insights into customer opportunities</p>
      </div>

      <DemoDataNotice />

      <Filters
        uniqueValues={uniqueValues}
        filters={filters}
        onFiltersChange={setFilters}
      />

      {/* Stats Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
        <div className="bg-white rounded-xl shadow-sm p-6 text-center animate-slide-up">
          <h6 className="text-gray-600 mb-2 text-sm">Unique Industries</h6>
          <h3 className="text-3xl font-bold text-blue-600">
            {new Set(filteredCustomers.map(c => c.Industry_Vertical)).size}
          </h3>
        </div>
        <div className="bg-white rounded-xl shadow-sm p-6 text-center animate-slide-up" style={{ animationDelay: '0.1s' }}>
          <h6 className="text-gray-600 mb-2 text-sm">Cloud Platforms</h6>
          <h3 className="text-3xl font-bold text-blue-500">
            {new Set(filteredCustomers.map(c => c.Cloud_Platforms)).size}
          </h3>
        </div>
        <div className="bg-white rounded-xl shadow-sm p-6 text-center animate-slide-up" style={{ animationDelay: '0.2s' }}>
          <h6 className="text-gray-600 mb-2 text-sm">Avg Cloud Opt</h6>
          <h3 className="text-3xl font-bold text-green-600">
            {filteredCustomers.length > 0
              ? (filteredCustomers.reduce((sum, c) => sum + c.Cloud_Optimization_Potential, 0) / filteredCustomers.length).toFixed(1)
              : '0.0'}%
          </h3>
        </div>
        <div className="bg-white rounded-xl shadow-sm p-6 text-center animate-slide-up" style={{ animationDelay: '0.3s' }}>
          <h6 className="text-gray-600 mb-2 text-sm">Avg ELO Opt</h6>
          <h3 className="text-3xl font-bold text-orange-500">
            {filteredCustomers.length > 0
              ? (filteredCustomers.reduce((sum, c) => sum + c.ELO_Optimization_Potential, 0) / filteredCustomers.length).toFixed(1)
              : '0.0'}%
          </h3>
        </div>
      </div>

      {/* Charts */}
      <div className="space-y-8">
        <div className="animate-fade-in">
          <h4 className="text-blue-600 text-xl font-bold mb-4 pb-2 border-b-2 border-blue-600 inline-block">
            License Ecosystem Usage
          </h4>
          <div className="bg-white rounded-xl shadow-sm p-6">
            <h5 className="text-center text-lg font-semibold mb-4">License Ecosystem Usage</h5>
            <div style={{ height: '600px' }}>
              <BarChart
                data={licenseData}
                xCol="License"
                yCol="Count"
                color={COLORS.primary}
              />
            </div>
          </div>
        </div>

        <div className="animate-fade-in" style={{ animationDelay: '0.1s' }}>
          <h4 className="text-blue-600 text-xl font-bold mb-4 pb-2 border-b-2 border-blue-600 inline-block">
            Optimization Potential by Region
          </h4>
          <div className="bg-white rounded-xl shadow-sm p-6">
            <h5 className="text-center text-lg font-semibold mb-4">Optimization Potential by Region</h5>
            <div style={{ height: '700px' }}>
              <GroupedBarChart
                data={regionSummary}
                xCol="Region"
                yCols={['Avg Cloud %', 'Avg ELO %']}
              />
            </div>
          </div>
        </div>

        <div className="animate-fade-in" style={{ animationDelay: '0.2s' }}>
          <h4 className="text-blue-600 text-xl font-bold mb-4 pb-2 border-b-2 border-blue-600 inline-block">
            Decision Maker Distribution
          </h4>
          <div className="bg-white rounded-xl shadow-sm p-6">
            <h5 className="text-center text-lg font-semibold mb-4">Decision Maker Distribution</h5>
            <div style={{ height: '600px' }}>
              <PieChart data={decisionMakerData} namesCol="Role" valuesCol="Count" />
            </div>
          </div>
        </div>

        {/* Key Insights */}
        <div className="bg-white rounded-xl shadow-sm animate-fade-in" style={{ animationDelay: '0.3s' }}>
          <div className="bg-blue-600 text-white p-4 rounded-t-xl">
            <h5 className="text-lg font-bold">Key Insights</h5>
          </div>
          <div className="p-6">
            <ul className="space-y-2 text-sm list-disc list-inside">
              <li>
                <strong>Top License System:</strong>{' '}
                {licenseData[0]?.License} used by {licenseData[0]?.Count} customers
              </li>
              <li>
                <strong>Highest Cloud Optimization:</strong>{' '}
                {filteredCustomers.length > 0 && (() => {
                  const max = Math.max(...filteredCustomers.map(c => c.Cloud_Optimization_Potential))
                  const customer = filteredCustomers.find(c => c.Cloud_Optimization_Potential === max)
                  return `${customer?.Customer_Name} with ${max}% potential`
                })()}
              </li>
              <li>
                <strong>Highest ELO Optimization:</strong>{' '}
                {filteredCustomers.length > 0 && (() => {
                  const max = Math.max(...filteredCustomers.map(c => c.ELO_Optimization_Potential))
                  const customer = filteredCustomers.find(c => c.ELO_Optimization_Potential === max)
                  return `${customer?.Customer_Name} with ${max}% potential`
                })()}
              </li>
              <li>
                <strong>Most Common Decision Maker:</strong>{' '}
                {decisionMakerData[0]?.Role} ({decisionMakerData[0]?.Count} customers)
              </li>
              <li>
                <strong>Top Industry:</strong>{' '}
                {(() => {
                  const industryCounts: Record<string, number> = {}
                  filteredCustomers.forEach(c => {
                    industryCounts[c.Industry_Vertical] = (industryCounts[c.Industry_Vertical] || 0) + 1
                  })
                  const top = Object.entries(industryCounts).sort((a, b) => b[1] - a[1])[0]
                  return `${top?.[0]} with ${top?.[1]} customers`
                })()}
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  )
}

