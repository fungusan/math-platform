import { writable } from 'svelte/store';
import { browser } from '$app/environment';
import { goto } from '$app/navigation';

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

export function checkAuthAndNavigate(targetPath: string, user: any) {
    if (!user) {
        goto('/login?error=unauthorized');
    } else {
        goto(targetPath);
    }
}