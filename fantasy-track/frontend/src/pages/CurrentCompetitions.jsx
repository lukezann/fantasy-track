import React, { useState, useEffect } from 'react'
import BackButton from '../components/BackButton'
import Spinner from '../components/Spinner'
import axios from 'axios'
import { useNavigate, useParams } from 'react-router-dom'

const CurrentCompetitions = () => {
  return (
    <div className='p-4'>
      <p> Current Competitions</p>
    </div>
  )
}

export default CurrentCompetitions