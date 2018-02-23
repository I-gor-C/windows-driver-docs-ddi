---
UID: NE:netdispumdddi.MIRACAST_STATUS
title: MIRACAST_STATUS
author: windows-driver-content
description: Specifies status types that the user-mode display driver uses to report Miracast connection status.
old-location: display\miracast_status.htm
old-project: display
ms.assetid: 26949ef9-ddcd-496d-b7e2-7c971bfaf3fb
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: MIRACAST_STATUS_MISSING_KEEPALIVE, netdispumdddi/MIRACAST_STATUS_INSUFFICIENT_BANDWIDTH, netdispumdddi/MIRACAST_STATUS_CRITICAL_ERROR, MIRACAST_STATUS, netdispumdddi/MIRACAST_STATUS_FORCE_UINT32, MIRACAST_STATUS_CRITICAL_ERROR, MIRACAST_STATUS_INSUFFICIENT_BANDWIDTH, netdispumdddi/MIRACAST_STATUS_MISSING_KEEPALIVE, MIRACAST_STATUS_SINK_FAILED_STANDARD_MODE_CHANGE, MIRACAST_STATUS enumeration [Display Devices], netdispumdddi/MIRACAST_STATUS_SINK_FAILED_STANDARD_MODE_CHANGE, MIRACAST_STATUS_FORCE_UINT32, MIRACAST_STATUS_SINK_DISOCNNECT_REQUEST, display.miracast_status, netdispumdddi/MIRACAST_STATUS, netdispumdddi/MIRACAST_STATUS_SINK_DISOCNNECT_REQUEST
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	Netdispumdddi.h
apiname:
-	MIRACAST_STATUS
product: Windows
targetos: Windows
req.typenames: MIRACAST_STATUS
---

# MIRACAST_STATUS Enumeration
Specifies status types  that the user-mode display driver uses to report Miracast connection status.

## Syntax
````
typedef enum  { 
  MIRACAST_STATUS_CRITICAL_ERROR                    = 0,
  MIRACAST_STATUS_MISSING_KEEPALIVE                 = 1,
  MIRACAST_STATUS_SINK_DISOCNNECT_REQUEST           = 2,
  MIRACAST_STATUS_INSUFFICIENT_BANDWIDTH            = 3,
  MIRACAST_STATUS_SINK_FAILED_STANDARD_MODE_CHANGE  = 4,
  MIRACAST_STATUS_FORCE_UINT32                      = 0xffffffff
} MIRACAST_STATUS;
````

## Constants

<table>
            
                <tr>
                    <td>MIRACAST_STATUS_COMPANION_DRIVER_DISCONNECT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>MIRACAST_STATUS_CRITICAL_ERROR</td>
                    <td>An unspecified error occurred, and the Miracast connected session cannot continue.</td>
                </tr>
            
                <tr>
                    <td>MIRACAST_STATUS_FORCE_UINT32</td>
                    <td>Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. You should not use this value.</td>
                </tr>
            
                <tr>
                    <td>MIRACAST_STATUS_INSUFFICIENT_BANDWIDTH</td>
                    <td>The bandwidth of the wireless connection has changed such that the current mode cannot be sustained.</td>
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
                    <td>MIRACAST_STATUS_SINK_FAILED_STANDARD_MODE_CHANGE</td>
                    <td>The Miracast sink failed to set a standard Video Electronics Standards Association (VESA) setting, Consumer Electronics Association (CEA) standard setting, or a hand-held mode change.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows 8.1 |
| **Header** | netdispumdddi.h (include Netdispumdddi.h) |