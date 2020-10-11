import React from 'react'

const ListComponent = ({name, data, filter}) => {
    return (
        <div className="list-component">
        <h5 className="list-title">{name}</h5>
        <div className="list-container">
            {data.map((item, index) => {
                if  (filter !== "" && item[0].toLowerCase().search(filter.toLowerCase()) === -1) return ''
                return <li key={index}>{item[0]} - {item[1]}</li>
            })}
        </div>
        </div>
    )
}

export default ListComponent
