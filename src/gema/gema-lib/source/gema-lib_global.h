#ifndef GEMALIB_GLOBAL_H
#define GEMALIB_GLOBAL_H

#include <QtCore/qglobal.h>

#if defined(GEMALIB_LIBRARY)
#  define GEMALIBSHARED_EXPORT Q_DECL_EXPORT
#else
#  define GEMALIBSHARED_EXPORT Q_DECL_IMPORT
#endif

#endif // GEMALIB_GLOBAL_H
