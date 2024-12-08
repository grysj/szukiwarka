import React, { useEffect, useState } from "react";

function isNull(target) {
  for (var member in target) {
    if (target[member] == null) return false;
  }
  return true;
}

const Search = ({ data, ...props }) => {
  console.log("serch", data);

  return (
    <div>
      {data && <h1>Search results for: {data.query}</h1>}
      {data && <h4>Results fetched in {data.time}</h4>}
      <div className="search-results">
        {data &&
          data.results.map((obj) => {
            return (
              <div className="single-result">
                <a href={obj.href} target="_blank">
                  {obj.name}
                </a>
                <span>
                  <b>{obj.prob}</b>{" "}
                </span>
              </div>
            );
          })}
      </div>
    </div>
  );
};

export default Search;
