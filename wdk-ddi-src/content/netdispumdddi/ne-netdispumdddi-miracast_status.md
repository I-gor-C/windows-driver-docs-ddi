---
UID: NE:netdispumdddi.MIRACAST_STATUS
title: MIRACAST_STATUS
author: windows-driver-content
description: Specifies status types that the user-mode display driver uses to report Miracast connection status.
old-location: display\miracast_status.htm
old-project: display
ms.assetid: 26949ef9-ddcd-496d-b7e2-7c971bfaf3fb
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: MIRACAST_STATUS, MIRACAST_STATUS enumeration [Display Devices], MIRACAST_STATUS_CRITICAL_ERROR, MIRACAST_STATUS_FORCE_UINT32, MIRACAST_STATUS_INSUFFICIENT_BANDWIDTH, MIRACAST_STATUS_MISSING_KEEPALIVE, MIRACAST_STATUS_SINK_DISOCNNECT_REQUEST, MIRACAST_STATUS_SINK_FAILED_STANDARD_MODE_CHANGE, display.miracast_status, netdispumdddi/MIRACAST_STATUS, netdispumdddi/MIRACAST_STATUS_CRITICAL_ERROR, netdispumdddi/MIRACAST_STATUS_FORCE_UINT32, netdispumdddi/MIRACAST_STATUS_INSUFFICIENT_BANDWIDTH, netdispumdddi/MIRACAST_STATUS_MISSING_KEEPALIVE, netdispumdddi/MIRACAST_STATUS_SINK_DISOCNNECT_REQUEST, netdispumdddi/MIRACAST_STATUS_SINK_FAILED_STANDARD_MODE_CHANGE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: netdispumdddi.h
req.include-header: Netdispumdddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
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
-	Netdispumdddi.h
api_name:
-	MIRACAST_STATUS
product:
- Windows
targetos: Windows
req.typenames: MIRACAST_STATUS
---

# MIRACAST_STATUS Enumeration
Specifies status types  that the user-mode display driver uses to report Miracast connection status.

## Syntax
```
typedef enum MIRACAST_STATUS {
  MIRACAST_STATUS_CRITICAL_ERROR                    ,
  MIRACAST_STATUS_MISSING_KEEPALIVE                 ,
  MIRACAST_STATUS_SINK_DISOCNNECT_REQUEST           ,
  MIRACAST_STATUS_INSUFFICIENT_BANDWIDTH            ,
  MIRACAST_STATUS_SINK_FAILED_STANDARD_MODE_CHANGE  ,
  MIRACAST_STATUS_COMPANION_DRIVER_DISCONNECT       ,
  MIRACAST_STATUS_FORCE_UINT32
} ;
```

## Constants

<table>
            
                <tr>
                    <td>MIRACAST_STATUS_CRITICAL_ERROR</td>
                    <td>An unspecified error occurred, and the Miracast connected session cannot continue.</td>
                </tr>
            
                <tr>
                    <td>MIRACAST_STATUS_MISSING_KEEPALIVE</td>
                    <td>The Miracast sink failed to respond to the protocol keep-alive message.</td>
                </tr>
            
                <tr>
                    <td>MIRACAST_STATUS_SINK_DISOCNNECT_REQUEST</td>
                    <td>The Miracast sink requested that it be disconnected.</td>
                </tr>
            
                <tr>
                    <td>MIRACAST_STATUS_INSUFFICIENT_BANDWIDTH</td>
                    <td>The bandwidth of the wireless connection has changed such that the current mode cannot be sustained.</td>
                </tr>
            
                <tr>
                    <td>MIRACAST_STATUS_SINK_FAILED_STANDARD_MODE_CHANGE</td>
                    <td>The Miracast sink failed to set a standard Video Electronics Standards Association (VESA) setting, Consumer Electronics Association (CEA) standard setting, or a hand-held mode change.</td>
                </tr>
            
                <tr>
                    <td>MIRACAST_STATUS_COMPANION_DRIVER_DISCONNECT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>MIRACAST_STATUS_FORCE_UINT32</td>
                    <td>Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. You should not use this value.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows 8.1 |
| **Header** | netdispumdddi.h (include Netdispumdddi.h) |