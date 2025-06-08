function assignAspectRatio(img) {
    const aspectRatio = img.naturalWidth / img.naturalHeight;

    if (aspectRatio >= 0.95 && aspectRatio <= 1.05) {
        return'aspect-1-1';
    } else if (aspectRatio >= 1.30 && aspectRatio <= 1.35) {
        return'aspect-4-3';
    } else if (aspectRatio >= 0.72 && aspectRatio <= 0.78) {
        return'aspect-3-4';
    } else if (aspectRatio >= 1.75 && aspectRatio <= 1.85) {
        return'aspect-16-9';
    } else if (aspectRatio >= 0.52 && aspectRatio <= 0.58) {
        return'aspect-9-16';
    } else if (aspectRatio >= 1.5 && aspectRatio <= 1.7) {
        return'aspect-3-2';
    } else if (aspectRatio >= 0.58 && aspectRatio <= 0.68) {
        return'aspect-2-3';
    } else if (aspectRatio >= 2.8 && aspectRatio <= 3.2) {
        return'aspect-3-1';
    } else if (aspectRatio >= 0.28 && aspectRatio <= 0.38) {
        return'aspect-1-3';
    } else {
        // Default to 1:1 if no match found
        return'aspect-1-1';
    }

}
