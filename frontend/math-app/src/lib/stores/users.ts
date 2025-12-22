import { writable } from 'svelte/store';
import { browser } from '$app/environment';

export const user = writable(null); // { id, user_name } or null if logged out

// Initialize token from localStorage only if in browser
export const token = writable(browser ? localStorage.getItem('authToken') : null);

token.subscribe(value => {
    if (browser) {
        if (value) {
            localStorage.setItem('authToken', value);
        } else {
            localStorage.removeItem('authToken');
        }
    }
});