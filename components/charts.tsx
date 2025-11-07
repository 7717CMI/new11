'use client'

import dynamic from 'next/dynamic'
import { COLORS, COLOR_SEQUENCE } from '@/lib/types'

const Plot = dynamic(() => import('react-plotly.js'), { ssr: false })

interface ChartProps {
  data: any[]
  xCol: string
  yCol: string
  title?: string
  color?: string
}

interface PieChartProps {
  data: any[]
  namesCol: string
  valuesCol: string
  title?: string
}

interface GroupedBarChartProps {
  data: any[]
  xCol: string
  yCols: string[]
  title?: string
}

interface ScatterChartProps {
  data: any[]
  xCol: string
  yCol: string
  colorCol: string
  title?: string
}

export function BarChart({ data, xCol, yCol, title = '', color = COLORS.primary }: ChartProps) {
  const x = data.map(d => d[xCol])
  const y = data.map(d => d[yCol])
  
  // Use gradient colors for bars
  const barColors = data.map((_, i) => COLOR_SEQUENCE[i % COLOR_SEQUENCE.length])

  return (
    <Plot
      data={[
        {
          x,
          y,
          type: 'bar',
          marker: {
            color: barColors,
            line: { color: 'white', width: 2 },
          },
          text: y,
          textposition: 'outside',
          textfont: { size: 12, color: '#212529' },
          width: 0.7,
          hovertemplate: '<b>%{x}</b><br>Count: %{y}<extra></extra>',
        },
      ] as any}
      layout={{
        title: { text: title, x: 0.5, xanchor: 'center', font: { size: 16, color: '#212529' } },
        xaxis: {
          title: { text: xCol, font: { size: 14, color: '#212529' } },
          tickangle: -45,
          tickfont: { size: 11.5 },
          automargin: true,
          showgrid: false,
        },
        yaxis: {
          title: { text: yCol, font: { size: 14, color: '#212529' } },
          tickfont: { size: 11.5 },
          automargin: true,
          showgrid: true,
          gridcolor: 'rgba(200,200,200,0.3)',
          gridwidth: 1,
        },
        template: 'plotly_white' as any,
        height: 530,
        margin: { l: 60, r: 100, t: 100, b: 180 },
        font: { family: 'Arial, sans-serif', size: 12 },
        plot_bgcolor: 'rgba(248,249,250,0.3)',
        paper_bgcolor: 'rgba(0,0,0,0)',
        bargap: 0.2,
      }}
      config={{ displayModeBar: false }}
      style={{ width: '100%', height: '100%' }}
    />
  )
}

export function PieChart({ data, namesCol, valuesCol, title = '' }: PieChartProps) {
  const labels = data.map(d => d[namesCol])
  const values = data.map(d => d[valuesCol])

  return (
    <Plot
      data={[
        {
          labels,
          values,
          type: 'pie',
          marker: {
            colors: COLOR_SEQUENCE,
            line: { color: 'white', width: 2 },
          },
          textposition: 'auto',
          textinfo: 'label+percent' as any,
          textfont: { size: 11, color: '#212529' },
          insidetextfont: { size: 11, color: 'white' },
          outsidetextfont: { size: 11, color: '#212529' },
          hovertemplate: '<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}<extra></extra>',
          pull: Array(labels.length).fill(0.02),
          hole: 0.3,
        },
      ] as any}
      layout={{
        title: { text: title, x: 0.5, xanchor: 'center', font: { size: 16, color: '#212529' } },
        template: 'plotly_white' as any,
        height: 520,
        margin: { l: 20, r: 240, t: 100, b: 60 },
        font: { family: 'Arial, sans-serif', size: 12 },
        showlegend: true,
        legend: {
          orientation: 'v',
          yanchor: 'top',
          y: 0.98,
          xanchor: 'left',
          x: 1.05,
          font: { size: 11 },
          itemsizing: 'constant',
          bgcolor: 'rgba(255,255,255,0.9)',
          bordercolor: '#ddd',
          borderwidth: 1,
        },
      }}
      config={{ displayModeBar: false }}
      style={{ width: '100%', height: '100%' }}
    />
  )
}

export function GroupedBarChart({ data, xCol, yCols, title = '' }: GroupedBarChartProps) {
  const traces = yCols.map((col, i) => ({
    name: col,
    x: data.map(d => d[xCol]),
    y: data.map(d => d[col]),
    type: 'bar' as const,
    marker: {
      color: COLOR_SEQUENCE[i % COLOR_SEQUENCE.length],
      line: { color: 'white', width: 1.5 },
    },
    text: data.map(d => d[col].toFixed(1)),
    textposition: 'outside' as const,
    textfont: { size: 11 },
    hovertemplate: `<b>%{x}</b><br>${col}: %{y:.1f}%<extra></extra>`,
    width: 0.4,
  }))

  return (
    <Plot
      data={traces as any}
      layout={{
        title: { text: title, x: 0.5, xanchor: 'center', font: { size: 16, color: '#212529' } },
        xaxis: {
          title: { text: xCol, font: { size: 13, color: '#212529' } },
          tickangle: -45,
          tickfont: { size: 10.5 },
          automargin: true,
          showgrid: false,
        },
        yaxis: {
          title: { text: 'Optimization Potential (%)', font: { size: 13, color: '#212529' } },
          tickfont: { size: 11 },
          automargin: true,
          showgrid: true,
          gridcolor: 'rgba(200,200,200,0.3)',
          gridwidth: 1,
        },
        barmode: 'group',
        template: 'plotly_white' as any,
        height: 620,
        margin: { l: 60, r: 100, t: 100, b: 280 },
        font: { family: 'Arial, sans-serif', size: 12 },
        legend: {
          orientation: 'h',
          yanchor: 'bottom',
          y: -0.65,
          xanchor: 'center',
          x: 0.5,
          font: { size: 12 },
          bgcolor: 'rgba(255,255,255,0.9)',
          bordercolor: '#ddd',
          borderwidth: 1,
        },
        plot_bgcolor: 'rgba(248,249,250,0.3)',
        paper_bgcolor: 'rgba(0,0,0,0)',
        bargap: 0.3,
        bargroupgap: 0.1,
      }}
      config={{ displayModeBar: false }}
      style={{ width: '100%', height: '100%' }}
    />
  )
}

export function StackedBarChart({ data, xCol, yCols, title = '' }: GroupedBarChartProps) {
  const traces = yCols.map((col, i) => ({
    name: col,
    x: data.map(d => d[xCol]),
    y: data.map(d => d[col]),
    type: 'bar' as const,
    marker: {
      color: COLOR_SEQUENCE[i % COLOR_SEQUENCE.length],
      line: { color: 'white', width: 1.5 },
    },
    text: data.map(d => (d[col] >= 10 ? d[col].toFixed(0) : '')),
    textposition: 'inside' as const,
    textfont: { size: 13, color: 'white' },
    hovertemplate: `<b>%{x}</b><br>${col}: %{y:.1f}<extra></extra>`,
    width: 0.9,
  }))

  return (
    <Plot
      data={traces as any}
      layout={{
        title: { text: title, x: 0.5, xanchor: 'center', font: { size: 20, color: '#212529' } },
        xaxis: {
          title: { text: xCol, font: { size: 16, color: '#212529' } },
          tickangle: -40,
          tickfont: { size: 13 },
          automargin: true,
          showgrid: false,
          tickmode: 'linear',
          dtick: 1,
          ticklen: 5,
          tickwidth: 1,
          tickcolor: '#666',
          side: 'bottom',
        },
        yaxis: {
          title: { text: 'Optimization Potential (%)', font: { size: 16, color: '#212529' } },
          tickfont: { size: 13 },
          automargin: true,
          showgrid: true,
          gridcolor: 'rgba(200,200,200,0.3)',
          gridwidth: 1,
        },
        barmode: 'stack',
        template: 'plotly_white' as any,
        height: 750,
        margin: { l: 90, r: 120, t: 120, b: 550 },
        font: { family: 'Arial, sans-serif', size: 14 },
        legend: {
          orientation: 'h',
          yanchor: 'bottom',
          y: -1.15,
          xanchor: 'center',
          x: 0.5,
          font: { size: 14 },
          bgcolor: 'rgba(255,255,255,0.9)',
          bordercolor: '#ddd',
          borderwidth: 1,
          itemwidth: 80,
          tracegroupgap: 30,
        },
        plot_bgcolor: 'rgba(248,249,250,0.3)',
        paper_bgcolor: 'rgba(0,0,0,0)',
        bargap: 0.15,
        bargroupgap: 0.0,
      }}
      config={{ displayModeBar: false }}
      style={{ width: '100%', height: '100%' }}
    />
  )
}

export function ScatterChart({ data, xCol, yCol, colorCol, title = '' }: ScatterChartProps) {
  const uniqueColors = [...new Set(data.map(d => d[colorCol]))]
  const traces = uniqueColors.map((colorVal, i) => {
    const filtered = data.filter(d => d[colorCol] === colorVal)
    return {
      x: filtered.map(d => d[xCol]),
      y: filtered.map(d => d[yCol]),
      mode: 'markers' as const,
      type: 'scatter' as const,
      name: colorVal,
      marker: {
        color: COLOR_SEQUENCE[i % COLOR_SEQUENCE.length],
        size: 12,
        line: { width: 1, color: 'white' },
      },
      text: filtered.map(d => d.Customer_Name),
      hovertemplate: '<b>%{text}</b><br>%{x}<br>%{y}<extra></extra>',
    }
  })

  return (
    <Plot
      data={traces as any}
      layout={{
        title: { text: title, x: 0.5, xanchor: 'center', font: { size: 16, color: '#212529' } },
        xaxis: {
          title: { text: xCol, font: { size: 13, color: '#212529' } },
          tickfont: { size: 11 },
          automargin: true,
        },
        yaxis: {
          title: { text: yCol, font: { size: 13, color: '#212529' } },
          tickfont: { size: 11 },
          automargin: true,
        },
        template: 'plotly_white' as any,
        height: 550,
        margin: { l: 50, r: 220, t: 80, b: 60 },
        font: { family: 'Arial, sans-serif', size: 12 },
        plot_bgcolor: 'rgba(0,0,0,0)',
        paper_bgcolor: 'rgba(0,0,0,0)',
        legend: {
          yanchor: 'middle',
          y: 0.5,
          xanchor: 'left',
          x: 1.02,
          font: { size: 10 },
          title: { text: colorCol, font: { size: 11 } },
        },
      }}
      config={{ displayModeBar: false }}
      style={{ width: '100%', height: '100%' }}
    />
  )
}

