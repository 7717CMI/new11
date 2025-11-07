# Filter Testing Guide

## Dashboard Status
✅ **Running successfully on: http://127.0.0.1:8050**

---

## How Filters Work

All filters in the sidebar are **reactive** and **multi-select**. When you change any filter:

1. ✅ The data store updates immediately
2. ✅ All visualizations re-render with filtered data
3. ✅ KPI cards recalculate metrics
4. ✅ Charts update to show only filtered customers
5. ✅ The data table refreshes

---

## Filter Testing Checklist

### 1. Industry Vertical Filter

**Test Steps:**
1. Open http://127.0.0.1:8050
2. In the sidebar, find **"Industry Vertical"** dropdown
3. Select one industry (e.g., "Food & Beverage")
4. **Expected Results:**
   - Overview page shows only Food & Beverage customers
   - Total Customers count decreases
   - Industry bar chart shows only selected industry
   - All percentages recalculate for filtered set

**Multi-Select Test:**
1. Select multiple industries (e.g., "Food & Beverage" + "Energy / Oil & Gas")
2. **Expected:** Charts show only the 2 selected industries

**Data Verification:**
- Go to Customer Details page
- Verify table shows only selected industries
- Count rows to confirm matches KPI card

✅ **Pass/Fail:** _________

---

### 2. Cloud Platform Filter

**Test Steps:**
1. Clear all filters (click "Reset Filters")
2. Select **"Cloud Platform"** → "Microsoft Azure"
3. **Expected Results:**
   - Only Azure customers displayed
   - Cloud Platform pie chart shows only Azure
   - Customer count updates
   - All Azure-specific metrics visible

**Multi-Cloud Test:**
1. Select "Multi-cloud (Azure + AWS)"
2. **Expected:** Shows only multi-cloud customers

**Cross-Page Test:**
1. Navigate to Analytics page
2. **Expected:** License ecosystem chart updates
3. Regional optimization chart shows only Azure customers

✅ **Pass/Fail:** _________

---

### 3. Geographic Region Filter

**Test Steps:**
1. Reset filters
2. Select **"Geographic Region"** → "Southeast U.S."
3. **Expected Results:**
   - Only SE customers displayed (Atlanta, Birmingham, etc.)
   - Regional groupings update
   - Customer count changes

**Verification:**
1. Go to Customer Details
2. Check "Geographical_Presence" column
3. All should contain "Southeast U.S."

✅ **Pass/Fail:** _________

---

### 4. Optimization Type Filter

**Test Steps:**
1. Reset filters
2. Select **"Optimization Type"** → "Both (Cloud FinOps + ELO)"
3. **Expected Results:**
   - Only customers with both optimization types shown
   - Optimization type pie chart updates
   - Grouped bar chart shows both Cloud and ELO values > 0

**Single Type Test:**
1. Select "Cloud FinOps" only
2. **Expected:**
   - ELO Opt % columns show 0
   - Only cloud optimization potential visible

✅ **Pass/Fail:** _________

---

### 5. License Ecosystem Filter

**Test Steps:**
1. Reset filters
2. Select **"License Ecosystem"** → "SAP HANA"
3. **Expected Results:**
   - Only customers with SAP HANA licenses shown
   - License ecosystem chart on Analytics page updates
   - SAP appears in all license ecosystem strings

**Multi-License Test:**
1. Select "Microsoft 365" + "Oracle Database"
2. **Expected:** Customers with either license shown

**Verification:**
1. Check Customer Details table
2. License_Ecosystem column contains selected values

✅ **Pass/Fail:** _________

---

### 6. Optimization Potential Range Slider

**Test Steps:**
1. Reset filters
2. Adjust slider to **20% - 30%**
3. **Expected Results:**
   - Only customers with 20-30% total optimization shown
   - High-value targets highlighted
   - Average optimization stays within 20-30% range

**Edge Case Test:**
1. Set slider to 0% - 10%
2. **Expected:** Low optimization customers (may be none)
3. Set slider to 40% - 50%
4. **Expected:** High optimization customers only

**KPI Verification:**
- Avg Optimization Potential should be within slider range
- Scatter plot points fall within Y-axis range

✅ **Pass/Fail:** _________

---

### 7. Reset Filters Button

**Test Steps:**
1. Apply multiple filters:
   - Industry: "Healthcare"
   - Cloud: "AWS"
   - Region: "Northeast U.S."
   - Opt Range: 15% - 25%
2. Click **"Reset Filters"** button
3. **Expected Results:**
   ✅ All dropdowns clear to empty
   ✅ Slider returns to 0% - 50%
   ✅ All 30 customers displayed
   ✅ All charts show full dataset

✅ **Pass/Fail:** _________

---

### 8. Combined Filter Test (Real-World Scenario)

**Scenario:** Find high-value Azure customers in Financial Services with strong optimization potential

**Steps:**
1. Reset filters
2. Set filters:
   - **Industry:** "Financial Services / Banking"
   - **Cloud Platform:** "Microsoft Azure"
   - **Optimization Type:** "Both (Cloud FinOps + ELO)"
   - **Opt Potential:** 25% - 50%

3. **Expected Results:**
   - Very specific subset of customers
   - May show 0-3 customers
   - All meet ALL criteria
   - KPIs reflect filtered set only

4. **Verify on Customer Details page:**
   - All customers are banks
   - All use Azure
   - All have both optimization types
   - All have 25-50% total potential

5. **Export Test:**
   - Click "Export to CSV"
   - Open exported file
   - Verify all rows match criteria

✅ **Pass/Fail:** _________

---

### 9. Page Navigation with Active Filters

**Test Steps:**
1. Apply filters:
   - Industry: "Retail"
   - Cloud: "AWS"
2. Navigate: **Overview → Customer Details → Analytics**
3. **Expected Results:**
   ✅ Filters persist across pages
   ✅ All pages show same filtered dataset
   ✅ No filter reset on page change
   ✅ Customer count consistent

4. Go back to Overview
5. **Expected:** Same filters still active

✅ **Pass/Fail:** _________

---

### 10. Empty Result Handling

**Test Steps:**
1. Reset filters
2. Apply impossible combination:
   - Industry: "Food & Beverage"
   - Cloud: "Google Cloud Platform"
   - License: "IBM Mainframe"
   - Opt Range: 45% - 50%

3. **Expected Results:**
   ✅ Alert message: "No customers match the selected filters"
   ✅ No error messages in console
   ✅ Charts don't crash
   ✅ Page remains functional

4. Adjust filters to valid combination
5. **Expected:** Data reappears smoothly

✅ **Pass/Fail:** _________

---

## Quantitative Data Filter Test

### Test: Financial Metrics Update

**Steps:**
1. Reset filters
2. Note "Total Customers" KPI
3. Apply filter: Industry = "Financial Services"
4. **Verify:**
   - Customer count decreases
   - All financial metrics recalculate:
     - Average IT Spend changes
     - Total Savings Potential updates
     - Cloud spend aggregates update

5. Go to Analytics page
6. **Check:**
   - All quantitative charts update
   - Savings calculations reflect filtered customers only

✅ **Pass/Fail:** _________

---

## Performance Test

### Test: Filter Response Time

**Acceptance Criteria:** Filters should update within 1 second

1. Apply Industry filter
   - **Time:** _____ seconds

2. Apply multi-select filter (3+ industries)
   - **Time:** _____ seconds

3. Apply all filters at once
   - **Time:** _____ seconds

4. Reset all filters
   - **Time:** _____ seconds

✅ **All under 1 second:** Yes / No

---

## Visual Verification Checklist

### Charts Update Correctly

- [ ] Overview: Industry bar chart
- [ ] Overview: Cloud platform pie chart
- [ ] Overview: Optimization type pie chart
- [ ] Overview: Optimization by industry grouped bar
- [ ] Overview: Scatter plot
- [ ] Customer Details: Data table
- [ ] Analytics: License ecosystem chart
- [ ] Analytics: Regional optimization chart
- [ ] Analytics: Cloud vs ELO stacked bar
- [ ] Analytics: Decision maker pie chart
- [ ] Analytics: Trigger events chart

---

## KPI Card Validation

When filters are applied, verify KPIs recalculate:

1. **Total Customers**
   - [ ] Decreases when filters applied
   - [ ] Shows count of visible customers

2. **Avg Optimization Potential**
   - [ ] Recalculates average for filtered set
   - [ ] Changes when high/low opt customers filtered

3. **Total Cloud Potential**
   - [ ] Sum updates for filtered customers
   - [ ] Goes to 0 when "ELO only" customers selected

4. **Total ELO Potential**
   - [ ] Sum updates for filtered customers
   - [ ] Goes to 0 when "Cloud only" customers selected

---

## Data Table Filter Test

### Customer Details Page Specific Tests

1. **Built-in Column Filters:**
   - Click on any column header filter
   - Type search term (e.g., "Azure" in Cloud Platform column)
   - **Expected:** Table filters in addition to sidebar filters

2. **Sorting:**
   - Click "Total Opt %" column header
   - **Expected:** Sorts descending (highest first)
   - Click again
   - **Expected:** Sorts ascending

3. **Pagination:**
   - Apply filter showing >20 customers
   - **Expected:** Pagination appears
   - Click "Next" page
   - **Expected:** Shows next 20 customers

4. **Row Selection:**
   - Click on any table row
   - **Expected:** Detailed customer card appears below
   - Select different row
   - **Expected:** Card updates to new customer

---

## Mobile Responsiveness Test (Optional)

If testing on mobile/tablet:

1. Open dashboard on mobile device
2. Verify hamburger menu appears
3. Click menu → Access filters
4. Apply filters
5. **Expected:** Works same as desktop

---

## Error Scenario Testing

### Test: Rapid Filter Changes

1. Rapidly click multiple filters in quick succession
2. **Expected:**
   - No errors in console
   - Dashboard doesn't freeze
   - Final state matches last filter selection

### Test: Browser Back Button

1. Apply filters
2. Click browser back button
3. **Expected:**
   - Stays on same page OR navigates correctly
   - No error messages

---

## Success Criteria

**Dashboard passes testing if:**

✅ All 10 main filter tests pass
✅ All KPIs update correctly
✅ All charts refresh with filtered data
✅ Customer count is consistent across pages
✅ Export CSV contains only filtered data
✅ No console errors during filtering
✅ Reset button clears all filters
✅ Empty results handled gracefully
✅ Performance: Filters respond within 1 second
✅ Data integrity: Numbers match filtered dataset

---

## Known Expected Behaviors

### Correct Behaviors (Not Bugs):

1. **Multi-select filters:**
   - Selecting multiple values uses OR logic
   - Example: Industry "Retail" OR "Banking" shows both

2. **Cross-filter behavior:**
   - Multiple filters use AND logic
   - Example: Industry "Retail" AND Cloud "Azure" shows only Retail+Azure

3. **Slider inclusive:**
   - Range 20-30% includes customers with exactly 20% or 30%

4. **License ecosystem partial match:**
   - Selecting "SAP" shows customers with ANY SAP product
   - Not just exact "SAP" - includes "SAP HANA", "SAP S/4HANA", etc.

5. **Region filter:**
   - Matches substring in "Geographical_Presence" field
   - "Southeast U.S." matches "operates across Southeast U.S."

---

## Troubleshooting

### If Filters Don't Work:

1. **Check console (F12):**
   - Look for JavaScript errors
   - Check callback errors

2. **Verify data loaded:**
   - Look for "Loaded X customer records" in terminal
   - Should show "Loaded 30 customer records"

3. **Clear browser cache:**
   - Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)

4. **Restart dashboard:**
   - Stop: Ctrl+C in terminal
   - Start: `python app.py`

---

## Test Results Summary

| Test Category | Status | Notes |
|---------------|--------|-------|
| Industry Filter | ⬜ | |
| Cloud Platform Filter | ⬜ | |
| Region Filter | ⬜ | |
| Optimization Type Filter | ⬜ | |
| License Ecosystem Filter | ⬜ | |
| Potential Range Slider | ⬜ | |
| Reset Filters | ⬜ | |
| Combined Filters | ⬜ | |
| Page Navigation | ⬜ | |
| Empty Results | ⬜ | |
| Quantitative Updates | ⬜ | |
| Performance | ⬜ | |
| Visual Charts | ⬜ | |
| KPI Cards | ⬜ | |
| Data Table | ⬜ | |

**Overall Status:** ⬜ PASS / ⬜ FAIL

---

## Next Steps After Testing

1. ✅ Document any bugs found
2. ✅ Test with real customer data
3. ✅ Share dashboard with stakeholders
4. ✅ Gather user feedback
5. ✅ Iterate based on usage patterns

---

**🎯 The dashboard is ready for testing at: http://127.0.0.1:8050**

**All filters should work immediately and update all visualizations in real-time!**
