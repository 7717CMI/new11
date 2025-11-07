'use client'

export function DemoDataNotice() {
  return (
    <div className="bg-yellow-50 border-2 border-yellow-400 rounded-lg p-4 mb-6 shadow-sm">
      <div className="flex items-start">
        <div className="flex items-center mr-3">
          <div className="w-6 h-6 rounded-full bg-yellow-400 flex items-center justify-center mr-2">
            <i className="bi bi-exclamation-circle-fill text-yellow-600 text-sm"></i>
          </div>
          <div className="w-2 h-2 rounded-full bg-yellow-400 mr-2"></div>
          <h3 className="text-base font-bold text-yellow-900">
            Demo Data Notice
          </h3>
        </div>
      </div>
      <p className="text-sm text-yellow-800 mt-2 ml-8">
        This dashboard uses synthetic/demo data for illustration purposes only. No real-world customer data is associated with this application.
      </p>
    </div>
  )
}

