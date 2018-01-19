---
UID : NS:sti._STISUBSCRIBE
title : _STISUBSCRIBE
author : windows-driver-content
description : The STISUBSCRIBE structure is used as a parameter for the IStiDevice::Subscribe method.
old-location : image\stisubscribe.htm
old-project : image
ms.assetid : 68859180-274d-44f8-9ccf-1cae0348f902
ms.author : windowsdriverdev
ms.date : 1/17/2018
ms.keywords : _STISUBSCRIBE, STISUBSCRIBE, *LPSTISUBSCRIBE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : sti.h
req.include-header : Sti.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : STISUBSCRIBE
req.alt-loc : sti.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : STISUBSCRIBE, *LPSTISUBSCRIBE
req.product : Windows 10 or later.
---

# _STISUBSCRIBE structure
The STISUBSCRIBE structure is used as a parameter for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543768">IStiDevice::Subscribe</a> method.

## Syntax
````
typedef struct _STISUBSCRIBE {
  DWORD  dwSize;
  DWORD  dwFlags;
  DWORD  dwFilter;
  HWND   hWndNotify;
  HANDLE hEvent;
  UINT   uiNotificationMessage;
} STISUBSCRIBE, *LPSTISUBSCRIBE;
````

## Members

        
            `dwFilter`

            Reserved for system use.
        
            `dwFlags`

            One of the following bit flags, defined in <i>Sti.h</i>.
        
            `dwSize`

            Caller-supplied size, in bytes, of the STISUBSCRIBE structure.
        
            `hEvent`

            Handle to a Win32 event created with <b>CreateEvent</b>, which the event monitor will use with <b>SetEvent</b> when an event occurs and for which the application can wait. Used only if STI_SUBSCRIBE_FLAG_WINDOW is set in <b>dwFlags</b>.
        
            `hWndNotify`

            Handle to an application window that should receive the message specified by <b>uiNotificationMessage</b> when an event occurs. Used only if STI_SUBSCRIBE_FLAG_WINDOW is set in <b>dwFlags</b>.
        
            `uiNotificationMessage`

            Window message that should be passed to the <b>dwWndNotify</b> window when an event occurs.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | sti.h (include Sti.h) |