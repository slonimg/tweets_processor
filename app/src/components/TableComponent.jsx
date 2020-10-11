import React from 'react';
import ListComponent from './ListComponent'

const TableComponent = ({data, filter}) => {
    return (

        <div className="table-component">
            <div className="table-container">
                <ListComponent name="Top Words" data={data.words} filter={filter}/>
                <ListComponent name="Top Users" data={data.users} filter={filter}/>
                <ListComponent name="Top Hashtags" data={data.hashtags} filter={filter}/>
            </div>
            <h2 className="tweets_counter">Avg. tweets processed per second: {data.avg_tweets_per_second}</h2>
            <h2 className="tweets_counter">Total tweets processed: {data.total_tweets_processed}</h2>
        </div>
    )

}

export default TableComponent
