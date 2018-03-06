---
UID: NE:wditypes._WDI_WPS_CONFIGURATION_METHOD
title: "_WDI_WPS_CONFIGURATION_METHOD"
author: windows-driver-content
description: The WDI_WPS_CONFIGURATION_METHOD enumeration defines WPS configuration methods.
old-location: netvista\wdi_wps_configuration_method.htm
old-project: netvista
ms.assetid: 116B19BD-959F-4711-B3FB-9880539B7849
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: WDI_WPS_CONFIGURATION_METHOD, WDI_WPS_CONFIGURATION_METHOD enumeration [Network Drivers Starting with Windows Vista], WDI_WPS_CONFIGURATION_METHOD_DISPLAY, WDI_WPS_CONFIGURATION_METHOD_KEYPAD, WDI_WPS_CONFIGURATION_METHOD_NFC_INTERFACE, WDI_WPS_CONFIGURATION_METHOD_NFC_TAG, WDI_WPS_CONFIGURATION_METHOD_NULL, WDI_WPS_CONFIGURATION_METHOD_PUSHBUTTON, WDI_WPS_CONFIGURATION_METHOD_WFDS_DEFAULT, _WDI_WPS_CONFIGURATION_METHOD, netvista.wdi_wps_configuration_method, wditypes/WDI_WPS_CONFIGURATION_METHOD, wditypes/WDI_WPS_CONFIGURATION_METHOD_DISPLAY, wditypes/WDI_WPS_CONFIGURATION_METHOD_KEYPAD, wditypes/WDI_WPS_CONFIGURATION_METHOD_NFC_INTERFACE, wditypes/WDI_WPS_CONFIGURATION_METHOD_NFC_TAG, wditypes/WDI_WPS_CONFIGURATION_METHOD_NULL, wditypes/WDI_WPS_CONFIGURATION_METHOD_PUSHBUTTON, wditypes/WDI_WPS_CONFIGURATION_METHOD_WFDS_DEFAULT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wditypes.hpp
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	wditypes.hpp
api_name:
-	WDI_WPS_CONFIGURATION_METHOD
product: Windows
targetos: Windows
req.typenames: WDI_WPS_CONFIGURATION_METHOD
req.product: Windows 10 or later.
---

# _WDI_WPS_CONFIGURATION_METHOD Enumeration
The WDI_WPS_CONFIGURATION_METHOD enumeration defines WPS configuration methods.

## Syntax
````
typedef enum _WDI_WPS_CONFIGURATION_METHOD { 
  WDI_WPS_CONFIGURATION_METHOD_NULL           = 0,
  WDI_WPS_CONFIGURATION_METHOD_DISPLAY        = 0x0008,
  WDI_WPS_CONFIGURATION_METHOD_NFC_TAG        = 0x0020,
  WDI_WPS_CONFIGURATION_METHOD_NFC_INTERFACE  = 0x0040,
  WDI_WPS_CONFIGURATION_METHOD_PUSHBUTTON     = 0x0080,
  WDI_WPS_CONFIGURATION_METHOD_KEYPAD         = 0x0100,
  WDI_WPS_CONFIGURATION_METHOD_WFDS_DEFAULT   = 0x1000
} WDI_WPS_CONFIGURATION_METHOD;
````

## Constants

<table>
            
                <tr>
                    <td>WDI_WPS_CONFIGURATION_METHOD_DISPLAY</td>
                    <td>Pin display.</td>
                </tr>
            
                <tr>
                    <td>WDI_WPS_CONFIGURATION_METHOD_DUMMY_MAX_VALUE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WDI_WPS_CONFIGURATION_METHOD_KEYPAD</td>
                    <td>Pin keypad.</td>
                </tr>
            
                <tr>
                    <td>WDI_WPS_CONFIGURATION_METHOD_NFC_INTERFACE</td>
                    <td>NFC interface.</td>
                </tr>
            
                <tr>
                    <td>WDI_WPS_CONFIGURATION_METHOD_NFC_TAG</td>
                    <td>NFC tag.</td>
                </tr>
            
                <tr>
                    <td>WDI_WPS_CONFIGURATION_METHOD_NULL</td>
                    <td>WFDS.</td>
                </tr>
            
                <tr>
                    <td>WDI_WPS_CONFIGURATION_METHOD_PUSHBUTTON</td>
                    <td>Push button.</td>
                </tr>
            
                <tr>
                    <td>WDI_WPS_CONFIGURATION_METHOD_WFDS_DEFAULT</td>
                    <td>WFDS.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | wditypes.hpp |