'use client'

import { useEffect, useState } from 'react'
import { loadCustomerData, applyFilters, getUniqueValues, FilterState, exportToCSV } from '@/lib/utils'
import { Customer } from '@/lib/types'
import { DemoDataNotice } from '@/components/demo-notice'

export default function CustomersPage() {
  const [customers, setCustomers] = useState<Customer[]>([])
  const [filteredCustomers, setFilteredCustomers] = useState<Customer[]>([])
  const [selectedRows, setSelectedRows] = useState<number[]>([])
  const [loading, setLoading] = useState(true)
  const [searchTerm, setSearchTerm] = useState('')
  const [sortConfig, setSortConfig] = useState<{ key: keyof Customer | null; direction: 'asc' | 'desc' }>({ key: null, direction: 'asc' })

  useEffect(() => {
    loadCustomerData().then((data) => {
      setCustomers(data)
      setFilteredCustomers(data)
      setLoading(false)
    })
  }, [])

  const handleExport = () => {
    const csv = exportToCSV(filteredCustomers)
    const blob = new Blob([csv], { type: 'text/csv' })
    const url = window.URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = 'customer_intelligence_export.csv'
    a.click()
    window.URL.revokeObjectURL(url)
  }

  const handleSort = (key: keyof Customer) => {
    let direction: 'asc' | 'desc' = 'asc'
    if (sortConfig.key === key && sortConfig.direction === 'asc') {
      direction = 'desc'
    }
    setSortConfig({ key, direction })
  }

  const sortedCustomers = [...filteredCustomers].sort((a, b) => {
    if (!sortConfig.key) return 0
    const aVal = a[sortConfig.key]
    const bVal = b[sortConfig.key]
    if (typeof aVal === 'number' && typeof bVal === 'number') {
      return sortConfig.direction === 'asc' ? aVal - bVal : bVal - aVal
    }
    const aStr = String(aVal || '')
    const bStr = String(bVal || '')
    return sortConfig.direction === 'asc' 
      ? aStr.localeCompare(bStr)
      : bStr.localeCompare(aStr)
  })

  const searchedCustomers = searchTerm
    ? sortedCustomers.filter(c => 
        Object.values(c).some(val => 
          String(val).toLowerCase().includes(searchTerm.toLowerCase())
        )
      )
    : sortedCustomers

  const formatNumber = (num: number, decimals = 0) => {
    return new Intl.NumberFormat('en-US', {
      minimumFractionDigits: decimals,
      maximumFractionDigits: decimals,
    }).format(num)
  }

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="text-lg text-gray-600">Loading...</div>
      </div>
    )
  }

  const selectedCustomer = selectedRows.length > 0 ? searchedCustomers[selectedRows[0]] : null

  return (
    <div className="max-w-7xl mx-auto page-container">
      <div className="mb-6">
        <h2 className="text-2xl font-bold text-gray-800 mb-1">Customer Details</h2>
        <p className="text-gray-600">Detailed customer information and contact details</p>
      </div>

      <DemoDataNotice />

      <div className="flex flex-col sm:flex-row gap-4 mb-4">
        <div className="flex-1">
          <input
            type="text"
            placeholder="Search customers..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full p-2.5 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-primary focus:border-transparent"
          />
        </div>
        <button
          onClick={handleExport}
          className="bg-primary text-white px-6 py-2.5 rounded-lg hover:bg-primary/90 transition-colors font-semibold text-sm flex items-center justify-center"
        >
          <i className="bi bi-download mr-2"></i>
          Export to CSV
        </button>
      </div>

      <div className="bg-white rounded-xl shadow-sm overflow-hidden mb-6">
        <div className="overflow-x-auto">
          <table className="w-full border-collapse text-sm">
            <thead>
              <tr className="bg-primary text-white">
                <th className="p-3 text-left font-semibold border border-gray-300 cursor-pointer hover:bg-primary/90" onClick={() => handleSort('Sr_No')}>
                  Sr No {sortConfig.key === 'Sr_No' && (sortConfig.direction === 'asc' ? '↑' : '↓')}
                </th>
                <th className="p-3 text-left font-semibold border border-gray-300 cursor-pointer hover:bg-primary/90" onClick={() => handleSort('Customer_Name')}>
                  Customer Name {sortConfig.key === 'Customer_Name' && (sortConfig.direction === 'asc' ? '↑' : '↓')}
                </th>
                <th className="p-3 text-left font-semibold border border-gray-300 cursor-pointer hover:bg-primary/90" onClick={() => handleSort('Industry_Vertical')}>
                  Industry {sortConfig.key === 'Industry_Vertical' && (sortConfig.direction === 'asc' ? '↑' : '↓')}
                </th>
                <th className="p-3 text-left font-semibold border border-gray-300">Cloud Platform</th>
                <th className="p-3 text-left font-semibold border border-gray-300 cursor-pointer hover:bg-primary/90" onClick={() => handleSort('Annual_IT_Spend_M')}>
                  IT Spend ($M) {sortConfig.key === 'Annual_IT_Spend_M' && (sortConfig.direction === 'asc' ? '↑' : '↓')}
                </th>
                <th className="p-3 text-left font-semibold border border-gray-300">Cloud Spend ($M)</th>
                <th className="p-3 text-left font-semibold border border-gray-300">License Spend ($M)</th>
                <th className="p-3 text-left font-semibold border border-gray-300">Cloud Savings ($M)</th>
                <th className="p-3 text-left font-semibold border border-gray-300">License Savings ($M)</th>
                <th className="p-3 text-left font-semibold border border-gray-300 cursor-pointer hover:bg-primary/90" onClick={() => handleSort('Total_Potential_Savings_M')}>
                  Total Savings ($M) {sortConfig.key === 'Total_Potential_Savings_M' && (sortConfig.direction === 'asc' ? '↑' : '↓')}
                </th>
                <th className="p-3 text-left font-semibold border border-gray-300">Cloud Opt %</th>
                <th className="p-3 text-left font-semibold border border-gray-300">ELO Opt %</th>
                <th className="p-3 text-left font-semibold border border-gray-300 cursor-pointer hover:bg-primary/90" onClick={() => handleSort('Total_Optimization_Potential')}>
                  Total Opt % {sortConfig.key === 'Total_Optimization_Potential' && (sortConfig.direction === 'asc' ? '↑' : '↓')}
                </th>
                <th className="p-3 text-left font-semibold border border-gray-300">Employees</th>
                <th className="p-3 text-left font-semibold border border-gray-300">IT Team</th>
                <th className="p-3 text-left font-semibold border border-gray-300">Decision Maker</th>
                <th className="p-3 text-left font-semibold border border-gray-300">Email</th>
              </tr>
            </thead>
            <tbody>
              {searchedCustomers.map((customer, index) => (
                <tr
                  key={customer.Sr_No}
                  onClick={() => setSelectedRows([index])}
                  className={`cursor-pointer hover:bg-gray-50 ${
                    selectedRows.includes(index) ? 'bg-primary/10' : index % 2 === 0 ? 'bg-white' : 'bg-gray-50'
                  }`}
                >
                  <td className="p-3 border border-gray-200">{customer.Sr_No}</td>
                  <td className="p-3 border border-gray-200 font-medium">{customer.Customer_Name}</td>
                  <td className="p-3 border border-gray-200">{customer.Industry_Vertical}</td>
                  <td className="p-3 border border-gray-200">{customer.Cloud_Platforms}</td>
                  <td className="p-3 border border-gray-200">{formatNumber(customer.Annual_IT_Spend_M)}</td>
                  <td className="p-3 border border-gray-200">{formatNumber(customer.Current_Cloud_Spend_M, 2)}</td>
                  <td className="p-3 border border-gray-200">{formatNumber(customer.Current_License_Spend_M, 2)}</td>
                  <td className="p-3 border border-gray-200">{formatNumber(customer.Potential_Cloud_Savings_M, 2)}</td>
                  <td className="p-3 border border-gray-200">{formatNumber(customer.Potential_License_Savings_M, 2)}</td>
                  <td className="p-3 border border-gray-200 font-bold text-success">
                    ${formatNumber(customer.Total_Potential_Savings_M, 2)}M
                  </td>
                  <td className="p-3 border border-gray-200">{customer.Cloud_Optimization_Potential}%</td>
                  <td className="p-3 border border-gray-200">{customer.ELO_Optimization_Potential}%</td>
                  <td className="p-3 border border-gray-200 font-bold text-success">
                    {customer.Total_Optimization_Potential}%
                  </td>
                  <td className="p-3 border border-gray-200">{formatNumber(customer.Number_of_Employees)}</td>
                  <td className="p-3 border border-gray-200">{formatNumber(customer.IT_Team_Size)}</td>
                  <td className="p-3 border border-gray-200">{customer.Decision_Maker}</td>
                  <td className="p-3 border border-gray-200">{customer.Email}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {searchedCustomers.length === 0 && (
        <div className="bg-warning/10 border-l-4 border-warning p-4 rounded-lg mb-4">
          <p className="text-gray-700">No customers found matching your search criteria.</p>
        </div>
      )}

      {selectedCustomer && (
        <div className="mt-6 bg-white rounded-xl shadow-sm p-6">
          <div className="bg-primary text-white p-4 rounded-t-xl mb-4">
            <h4 className="text-xl font-bold">{selectedCustomer.Customer_Name}</h4>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <h6 className="text-primary font-semibold mb-3">Overview</h6>
              <p className="text-sm mb-2"><strong>Industry:</strong> {selectedCustomer.Industry_Vertical}</p>
              <p className="text-sm mb-2"><strong>Location:</strong> {selectedCustomer.Geographical_Presence}</p>
              <p className="text-sm"><strong>Product Offering:</strong> {selectedCustomer.Product_Offering}</p>
            </div>
            <div>
              <h6 className="text-primary font-semibold mb-3">Technical Details</h6>
              <p className="text-sm mb-2"><strong>Cloud Platform:</strong> {selectedCustomer.Cloud_Platforms}</p>
              <p className="text-sm mb-2"><strong>License Ecosystem:</strong> {selectedCustomer.License_Ecosystem}</p>
              <p className="text-sm"><strong>Optimization Type:</strong> {selectedCustomer.Optimization_Type}</p>
            </div>
            <div>
              <h6 className="text-success font-semibold mb-3">Optimization Potential</h6>
              <p className="text-sm mb-2"><strong>Cloud Optimization:</strong> {selectedCustomer.Cloud_Optimization_Potential}%</p>
              <p className="text-sm mb-2"><strong>ELO Optimization:</strong> {selectedCustomer.ELO_Optimization_Potential}%</p>
              <p className="text-sm font-bold text-success"><strong>Total Potential:</strong> {selectedCustomer.Total_Optimization_Potential}%</p>
            </div>
            <div>
              <h6 className="text-info font-semibold mb-3">Contact Information</h6>
              <p className="text-sm mb-2"><strong>Decision Maker:</strong> {selectedCustomer.Decision_Maker}</p>
              <p className="text-sm mb-2"><strong>Phone:</strong> {selectedCustomer.Phone}</p>
              <p className="text-sm"><strong>Email:</strong> {selectedCustomer.Email}</p>
            </div>
            <div className="md:col-span-2">
              <h6 className="text-warning font-semibold mb-3">Business Context</h6>
              <p className="text-sm mb-2"><strong>Pain Points:</strong> {selectedCustomer.Pain_Points}</p>
              <p className="text-sm mb-2"><strong>Trigger Event:</strong> {selectedCustomer.Trigger_Event}</p>
              <p className="text-sm"><strong>Key Stakeholders:</strong> {selectedCustomer.Key_Stakeholders}</p>
            </div>
            <div className="md:col-span-2">
              <h6 className="text-primary font-semibold mb-3">Financial Metrics</h6>
              <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
                <div><strong>IT Spend:</strong> ${formatNumber(selectedCustomer.Annual_IT_Spend_M)}M</div>
                <div><strong>Cloud Spend:</strong> ${formatNumber(selectedCustomer.Current_Cloud_Spend_M, 2)}M</div>
                <div><strong>License Spend:</strong> ${formatNumber(selectedCustomer.Current_License_Spend_M, 2)}M</div>
                <div><strong>Total Savings:</strong> <span className="text-success font-bold">${formatNumber(selectedCustomer.Total_Potential_Savings_M, 2)}M</span></div>
              </div>
            </div>
            <div className="md:col-span-2">
              <h6 className="text-primary font-semibold mb-3">Infrastructure & Resources</h6>
              <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
                <div><strong>Employees:</strong> {formatNumber(selectedCustomer.Number_of_Employees)}</div>
                <div><strong>IT Team:</strong> {formatNumber(selectedCustomer.IT_Team_Size)}</div>
                <div><strong>VMs:</strong> {formatNumber(selectedCustomer.Number_of_VMs)}</div>
                <div><strong>Servers:</strong> {formatNumber(selectedCustomer.Physical_Servers)}</div>
                <div><strong>Databases:</strong> {formatNumber(selectedCustomer.Number_of_Databases)}</div>
                <div><strong>Applications:</strong> {formatNumber(selectedCustomer.Number_of_Applications)}</div>
                <div><strong>MS Licenses:</strong> {formatNumber(selectedCustomer.Microsoft_Licenses)}</div>
                <div><strong>SAP Licenses:</strong> {formatNumber(selectedCustomer.SAP_Licenses)}</div>
              </div>
            </div>
          </div>
        </div>
      )}

      {!selectedCustomer && searchedCustomers.length > 0 && (
        <div className="mt-6 bg-info/10 border-l-4 border-info p-4 rounded-lg">
          <p className="text-gray-700">
            Click on a row in the table above to view detailed customer information.
          </p>
        </div>
      )}
    </div>
  )
}

