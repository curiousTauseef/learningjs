import React, { Component } from 'react'
import PropTypes from 'prop-types'
import classNames from 'classnames'

class DropMenu extends Component {
  static propTypes = {
    /**
       Pass itemsList prop to give list of items to show on click of icon
     */
    itemsList: PropTypes.array.isRequired,
    /**
       Pass isDropUpMenu prop to show list above icon
     */
    isDropUpMenu: PropTypes.bool,
    /**
       Pass iconImageSrc prop to give path of icon
     */
    iconImageSrc: PropTypes.string.isRequired
  }

  static defaultProps = {
    isDropUpMenu: false
  }

  constructor (props, context) {
    super(props, context)
    this.state = {
      isListOpen: false
    }
  }

  onClickMenuItem = (item) => {
    item.onClick()
    this.setState({ isListOpen: false })
  }

  onClickIcon = () => {
    this.setState((previousState) => {
      return { isListOpen: !previousState.isListOpen }
    })
  }

  get getList () {
    const { props: { itemsList } } = this
    const listArray = itemsList && itemsList.map((item, index) => {
      return (<div key={index} className='item' onClick={() => this.onClickMenuItem(item)}>
        {item.name}
      </div>)
    })
    return listArray
  }

  render () {
    const { props: { isDropUpMenu, iconImageSrc }, state: { isListOpen } } = this
    const basicDropMenuClass = classNames({
      'basic-drop-menu ': true,
      'open': isListOpen
    })
    const listClass = classNames({
      'item-list ': true,
      'list-above ': isDropUpMenu,
      'list-below ': !isDropUpMenu
    })
    return (
      <div className={basicDropMenuClass}>
        <div className='profile-icon-section' onClick={this.onClickIcon}>
          <img className='profile-image-icon' src={iconImageSrc} alt='profile-image' />
        </div>
        <div className={listClass}>
          {this.getList}
        </div>
      </div>
    )
  }
}
export default DropMenu
