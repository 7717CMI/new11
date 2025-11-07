'use client'

import { useEffect, useState } from 'react'
import { loadCustomerData, applyFilters, getUniqueValues } from '@/lib/utils'
import { Customer, FilterState } from '@/lib/types'
import { Filters } from '@/components/filters'
import { BarChart, PieChart, GroupedBarChart, ScatterChart } from '@/components/charts'
import { COLORS } from '@/lib/types'
import { DemoDataNotice } from '@/components/demo-notice'

export default function OverviewPage() {
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

  // Calculate KPIs
  const totalCustomers = filteredCustomers.length
  const avgOptPotential = filteredCustomers.length > 0
    ? filteredCustomers.reduce((sum, c) => sum + c.Total_Optimization_Potential, 0) / filteredCustomers.length
    : 0
  const totalCloudOpt = filteredCustomers.reduce((sum, c) => sum + c.Cloud_Optimization_Potential, 0)
  const totalEloOpt = filteredCustomers.reduce((sum, c) => sum + c.ELO_Optimization_Potential, 0)

  // Industry distribution
  const industryCounts = filteredCustomers.reduce((acc, c) => {
    acc[c.Industry_Vertical] = (acc[c.Industry_Vertical] || 0) + 1
    return acc
  }, {} as Record<string, number>)
  const industryData = Object.entries(industryCounts)
    .map(([Industry, Count]) => ({ Industry, Count }))
    .sort((a, b) => b.Count - a.Count)
    .slice(0, 10)

  // Cloud platform distribution
  const cloudCounts = filteredCustomers.reduce((acc, c) => {
    acc[c.Cloud_Platforms] = (acc[c.Cloud_Platforms] || 0) + 1
    return acc
  }, {} as Record<string, number>)
  const cloudData = Object.entries(cloudCounts).map(([Platform, Count]) => ({ Platform, Count }))

  // Optimization type distribution
  const optTypeCounts = filteredCustomers.reduce((acc, c) => {
    acc[c.Optimization_Type] = (acc[c.Optimization_Type] || 0) + 1
    return acc
  }, {} as Record<string, number>)
  const optTypeData = Object.entries(optTypeCounts).map(([Type, Count]) => ({ Type, Count }))

  // Optimization potential by industry
  const optByIndustry = Object.entries(
    filteredCustomers.reduce((acc, c) => {
      if (!acc[c.Industry_Vertical]) {
        acc[c.Industry_Vertical] = { cloud: [], elo: [] }
      }
      acc[c.Industry_Vertical].cloud.push(c.Cloud_Optimization_Potential)
      acc[c.Industry_Vertical].elo.push(c.ELO_Optimization_Potential)
      return acc
    }, {} as Record<string, { cloud: number[], elo: number[] }>)
  ).map(([Industry, values]) => ({
    Industry,
    'Cloud Opt %': values.cloud.reduce((a, b) => a + b, 0) / values.cloud.length,
    'ELO Opt %': values.elo.reduce((a, b) => a + b, 0) / values.elo.length,
  })).slice(0, 8)

  return (
    <div className="max-w-7xl mx-auto page-container">
      <div className="mb-6">
        <h2 className="text-2xl font-bold text-gray-800 mb-1">Customer Intelligence Overview</h2>
        <p className="text-gray-600">Comprehensive view of customer optimization opportunities</p>
      </div>

      <DemoDataNotice />

      <Filters
        uniqueValues={uniqueValues}
        filters={filters}
        onFiltersChange={setFilters}
      />

      {filteredCustomers.length === 0 ? (
        <div className="bg-warning/10 border-l-4 border-warning p-4 rounded-lg mb-4">
          <div className="flex items-center">
            <i className="bi bi-exclamation-triangle-fill text-warning text-xl mr-3"></i>
            <span className="text-gray-700">
              No customers match the selected filters. Please adjust your filter criteria.
            </span>
          </div>
        </div>
      ) : (
        <>
          {/* KPI Cards */}
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
            <div className="bg-white rounded-xl shadow-sm p-6 hover:shadow-md transition-shadow animate-slide-up">
              <div className="flex items-center">
                <div className="mr-4">
                  <i className="bi bi-people-fill text-4xl text-blue-600"></i>
                </div>
                <div>
                  <p className="text-xs font-semibold text-gray-600 uppercase tracking-wide mb-1">
                    Total Customers
                  </p>
                  <p className="text-3xl font-bold text-gray-800">{totalCustomers}</p>
                  <p className="text-xs text-gray-500 mt-1">Active in database</p>
                </div>
              </div>
            </div>

            <div className="bg-white rounded-xl shadow-sm p-6 hover:shadow-md transition-shadow animate-slide-up" style={{ animationDelay: '0.1s' }}>
              <div className="flex items-center">
                <div className="mr-4">
                  <i className="bi bi-graph-up-arrow text-4xl text-green-600"></i>
                </div>
                <div>
                  <p className="text-xs font-semibold text-gray-600 uppercase tracking-wide mb-1">
                    Avg Optimization Potential
                  </p>
                  <p className="text-3xl font-bold text-gray-800">{avgOptPotential.toFixed(1)}%</p>
                  <p className="text-xs text-gray-500 mt-1">Combined Cloud + ELO</p>
                </div>
              </div>
            </div>

            <div className="bg-white rounded-xl shadow-sm p-6 hover:shadow-md transition-shadow animate-slide-up" style={{ animationDelay: '0.2s' }}>
              <div className="flex items-center">
                <div className="mr-4">
                  <i className="bi bi-cloud-arrow-up text-4xl text-blue-500"></i>
                </div>
                <div>
                  <p className="text-xs font-semibold text-gray-600 uppercase tracking-wide mb-1">
                    Total Cloud Potential
                  </p>
                  <p className="text-3xl font-bold text-gray-800">{totalCloudOpt.toFixed(0)}%</p>
                  <p className="text-xs text-gray-500 mt-1">Across all customers</p>
                </div>
              </div>
            </div>

            <div className="bg-white rounded-xl shadow-sm p-6 hover:shadow-md transition-shadow animate-slide-up" style={{ animationDelay: '0.3s' }}>
              <div className="flex items-center">
                <div className="mr-4">
                  <i className="bi bi-file-earmark-text text-4xl text-orange-500"></i>
                </div>
                <div>
                  <p className="text-xs font-semibold text-gray-600 uppercase tracking-wide mb-1">
                    Total ELO Potential
                  </p>
                  <p className="text-3xl font-bold text-gray-800">{totalEloOpt.toFixed(0)}%</p>
                  <p className="text-xs text-gray-500 mt-1">License optimization</p>
                </div>
              </div>
            </div>
          </div>

          <hr className="my-8 border-gray-200" />

          {/* Charts */}
          <div className="space-y-8">
            <div className="animate-fade-in">
              <h4 className="text-blue-600 text-xl font-bold mb-4 pb-2 border-b-2 border-blue-600 inline-block">
                Industry Analysis
              </h4>
              <div className="bg-white rounded-xl shadow-sm p-6">
                <h5 className="text-center text-lg font-semibold mb-4">
                  Top 10 Industries by Customer Count
                </h5>
                <div style={{ height: '580px' }}>
                  <BarChart
                    data={industryData}
                    xCol="Industry"
                    yCol="Count"
                    color={COLORS.primary}
                  />
                </div>
              </div>
            </div>

            <div className="animate-fade-in" style={{ animationDelay: '0.1s' }}>
              <h4 className="text-blue-600 text-xl font-bold mb-4 pb-2 border-b-2 border-blue-600 inline-block">
                Cloud Platform Distribution
              </h4>
              <div className="bg-white rounded-xl shadow-sm p-6">
                <h5 className="text-center text-lg font-semibold mb-4">
                  Cloud Platform Usage Across Customers
                </h5>
                <div style={{ height: '580px' }}>
                  <PieChart data={cloudData} namesCol="Platform" valuesCol="Count" />
                </div>
              </div>
            </div>

            <div className="animate-fade-in" style={{ animationDelay: '0.2s' }}>
              <h4 className="text-blue-600 text-xl font-bold mb-4 pb-2 border-b-2 border-blue-600 inline-block">
                Optimization Type Distribution
              </h4>
              <div className="bg-white rounded-xl shadow-sm p-6">
                <h5 className="text-center text-lg font-semibold mb-4">
                  Cloud FinOps vs ELO Distribution
                </h5>
                <div style={{ height: '580px' }}>
                  <PieChart data={optTypeData} namesCol="Type" valuesCol="Count" />
                </div>
              </div>
            </div>

            <div className="animate-fade-in" style={{ animationDelay: '0.3s' }}>
              <h4 className="text-blue-600 text-xl font-bold mb-4 pb-2 border-b-2 border-blue-600 inline-block">
                Optimization Potential by Industry
              </h4>
              <div className="bg-white rounded-xl shadow-sm p-6">
                <h5 className="text-center text-lg font-semibold mb-4">
                  Average Cloud & ELO Optimization Potential
                </h5>
                <div style={{ height: '680px' }}>
                  <GroupedBarChart
                    data={optByIndustry}
                    xCol="Industry"
                    yCols={['Cloud Opt %', 'ELO Opt %']}
                  />
                </div>
              </div>
            </div>

            <div className="animate-fade-in" style={{ animationDelay: '0.4s' }}>
              <h4 className="text-blue-600 text-xl font-bold mb-4 pb-2 border-b-2 border-blue-600 inline-block">
                Customer-Level Optimization Potential
              </h4>
              <div className="bg-white rounded-xl shadow-sm p-6">
                <h5 className="text-center text-lg font-semibold mb-4">
                  Total Optimization Potential by Customer (Color = Industry)
                </h5>
                <div style={{ height: '630px' }}>
                  <ScatterChart
                    data={filteredCustomers}
                    xCol="Sr_No"
                    yCol="Total_Optimization_Potential"
                    colorCol="Industry_Vertical"
                  />
                </div>
              </div>
            </div>
          </div>
        </>
      )}
    </div>
  )
}

