// src/lib/katex-contrib.d.ts
declare module 'katex/dist/contrib/auto-render.mjs' {
    import { KatexOptions } from 'katex';

    interface RenderMathInElementOptions extends KatexOptions {
        delimiters?: Array<{
            left: string;
            right: string;
            display: boolean;
        }>;
        ignoredTags?: string[];
        ignoredClasses?: string[];
        errorCallback?: (msg: string, err: Error) => void;
        preProcess?: (math: string) => string;
    }

    function renderMathInElement(
        elem: HTMLElement,
        options?: RenderMathInElementOptions
    ): void;

    export default renderMathInElement;
}