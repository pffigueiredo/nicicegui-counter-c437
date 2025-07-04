from nicegui.testing import User
from nicegui import ui


async def test_counter_initial_display(user: User) -> None:
    """Test that the counter displays correctly on page load."""
    await user.open('/')
    await user.should_see('Simple Counter')
    await user.should_see('Count: 0')


async def test_counter_increment(user: User) -> None:
    """Test that the increment button works correctly."""
    await user.open('/')
    
    # Initial state
    await user.should_see('Count: 0')
    
    # Click increment button
    increment_button = user.find('Increment')
    increment_button.click()
    await user.should_see('Count: 1')
    
    # Click increment button again
    increment_button.click()
    await user.should_see('Count: 2')


async def test_counter_decrement(user: User) -> None:
    """Test that the decrement button works correctly."""
    await user.open('/')
    
    # Initial state
    await user.should_see('Count: 0')
    
    # Click decrement button
    decrement_button = user.find('Decrement')
    decrement_button.click()
    await user.should_see('Count: -1')
    
    # Click decrement button again
    decrement_button.click()
    await user.should_see('Count: -2')


async def test_counter_increment_and_decrement(user: User) -> None:
    """Test that both increment and decrement buttons work together."""
    await user.open('/')
    
    # Initial state
    await user.should_see('Count: 0')
    
    # Increment twice
    increment_button = user.find('Increment')
    increment_button.click()
    increment_button.click()
    await user.should_see('Count: 2')
    
    # Decrement once
    decrement_button = user.find('Decrement')
    decrement_button.click()
    await user.should_see('Count: 1')
    
    # Decrement twice more
    decrement_button.click()
    decrement_button.click()
    await user.should_see('Count: -1')


async def test_counter_buttons_exist(user: User) -> None:
    """Test that both buttons are present and correctly styled."""
    await user.open('/')
    
    # Check that both buttons exist
    increment_button = user.find('Increment')
    decrement_button = user.find('Decrement')
    
    assert increment_button.elements, "Increment button should exist"
    assert decrement_button.elements, "Decrement button should exist"