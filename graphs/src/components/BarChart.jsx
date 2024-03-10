import React from 'react';
import { Bar, Line, Pie } from 'react-chartjs-2';
import ChartJS from 'chart.js/auto';

function BarChart({chartData}) {
    return (
        <Line data={chartData} />
    )
}

export default BarChart;