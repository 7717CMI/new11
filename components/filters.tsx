'use client'

import { useState } from 'react'
import { FilterState } from '@/lib/types'

interface FiltersProps {
  uniqueValues: {
    industries: string[]
    clouds: string[]
    regions: string[]
    optTypes: string[]
    licenses: string[]
  }
  filters: FilterState
  onFiltersChange: (filters: FilterState) => void
}

export function Filters({ uniqueValues, filters, onFiltersChange }: FiltersProps) {
  const [openDropdown, setOpenDropdown] = useState<string | null>(null)

  const updateFilter = (key: keyof FilterState, value: any) => {
    onFiltersChange({ ...filters, [key]: value })
  }

  const resetFilters = () => {
    onFiltersChange({
      industries: [],
      clouds: [],
      regions: [],
      optTypes: [],
      licenses: [],
      optRange: [0, 50],
    })
    setOpenDropdown(null)
  }

  const toggleDropdown = (name: string) => {
    setOpenDropdown(openDropdown === name ? null : name)
  }

  const handleMultiSelect = (key: keyof FilterState, value: string) => {
    const currentValues = filters[key] as string[]
    const newValues = currentValues.includes(value)
      ? currentValues.filter(v => v !== value)
      : [...currentValues, value]
    updateFilter(key, newValues)
  }

  const DropdownSelect = ({ 
    label, 
    name, 
    options, 
    selectedValues, 
    filterKey 
  }: { 
    label: string
    name: string
    options: string[]
    selectedValues: string[]
    filterKey: keyof FilterState
  }) => {
    const isOpen = openDropdown === name
    const displayText = selectedValues.length > 0 
      ? `${selectedValues.length} selected` 
      : `Select ${label.toLowerCase()}...`

    return (
      <div className="relative">
        <label className="block text-sm font-semibold text-gray-700 mb-2">
          {label}
        </label>
        <button
          type="button"
          onClick={() => toggleDropdown(name)}
                 className="w-full p-2.5 border border-gray-300 rounded-lg text-sm text-left bg-white hover:border-blue-600 focus:ring-2 focus:ring-blue-600 focus:border-transparent flex items-center justify-between"
        >
          <span className={selectedValues.length > 0 ? 'text-gray-900' : 'text-gray-500'}>
            {displayText}
          </span>
          <i className={`bi bi-chevron-${isOpen ? 'up' : 'down'} text-gray-400`}></i>
        </button>
        {isOpen && (
          <div className="absolute z-50 w-full mt-1 bg-white border border-gray-300 rounded-lg shadow-lg max-h-60 overflow-y-auto">
            {options.map((option) => {
              const isSelected = selectedValues.includes(option)
              return (
                <label
                  key={option}
                  className="flex items-center px-4 py-2 hover:bg-gray-50 cursor-pointer"
                >
                  <input
                    type="checkbox"
                    checked={isSelected}
                    onChange={() => handleMultiSelect(filterKey, option)}
                         className="mr-3 h-4 w-4 text-blue-600 focus:ring-blue-600 border-gray-300 rounded"
                  />
                  <span className="text-sm text-gray-700">{option}</span>
                </label>
              )
            })}
          </div>
        )}
      </div>
    )
  }

  return (
    <div className="bg-white rounded-xl border border-gray-200 p-4 mb-6 shadow-sm">
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-4">
        <DropdownSelect
          label="Industry Vertical"
          name="industry"
          options={uniqueValues.industries}
          selectedValues={filters.industries}
          filterKey="industries"
        />

        <DropdownSelect
          label="Cloud Platform"
          name="cloud"
          options={uniqueValues.clouds}
          selectedValues={filters.clouds}
          filterKey="clouds"
        />

        <DropdownSelect
          label="Geographic Region"
          name="region"
          options={uniqueValues.regions}
          selectedValues={filters.regions}
          filterKey="regions"
        />

        <DropdownSelect
          label="Optimization Type"
          name="optType"
          options={uniqueValues.optTypes}
          selectedValues={filters.optTypes}
          filterKey="optTypes"
        />
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <DropdownSelect
          label="License Ecosystem"
          name="license"
          options={uniqueValues.licenses}
          selectedValues={filters.licenses}
          filterKey="licenses"
        />

        <div>
          <label className="block text-sm font-semibold text-gray-700 mb-2">
            Optimization Potential Range (%)
          </label>
          <div className="space-y-2">
            <div className="flex items-center space-x-4">
              <input
                type="range"
                min="0"
                max="50"
                step="5"
                value={filters.optRange[0]}
                onChange={(e) => updateFilter('optRange', [parseInt(e.target.value), filters.optRange[1]])}
                className="flex-1 h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-primary"
              />
            </div>
            <div className="flex items-center space-x-4">
              <input
                type="range"
                min="0"
                max="50"
                step="5"
                value={filters.optRange[1]}
                onChange={(e) => updateFilter('optRange', [filters.optRange[0], parseInt(e.target.value)])}
                className="flex-1 h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-primary"
              />
            </div>
            <div className="text-center">
              <span className="text-sm font-medium text-gray-700">
                {filters.optRange[0]}% - {filters.optRange[1]}%
              </span>
            </div>
          </div>
        </div>

        <div className="flex items-end">
          <button
            onClick={resetFilters}
                 className="w-full bg-blue-600 text-white px-4 py-2.5 rounded-lg hover:bg-blue-700 transition-colors font-semibold text-sm flex items-center justify-center"
          >
            <i className="bi bi-arrow-clockwise mr-2"></i>
            Reset Filters
          </button>
        </div>
      </div>

      {/* Click outside to close dropdowns */}
      {openDropdown && (
        <div
          className="fixed inset-0 z-40"
          onClick={() => setOpenDropdown(null)}
        />
      )}
    </div>
  )
}

