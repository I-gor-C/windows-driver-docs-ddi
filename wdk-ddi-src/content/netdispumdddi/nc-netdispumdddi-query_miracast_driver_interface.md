---
UID: NC.netdispumdddi.QUERY_MIRACAST_DRIVER_INTERFACE
title: QUERY_MIRACAST_DRIVER_INTERFACE
author: windows-driver-content
description: Called by the operating system to query the Miracast user-mode driver interface, MIRACAST_DRIVER_INTERFACE.
old-location: display\querymiracastdriverinterface.htm
old-project: display
ms.assetid: a8833f8c-7e3f-422c-922e-e75476358ee9
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _NDK_SRQ, NDK_SRQ
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: netdispumdddi.h
req.include-header: Netdispumdddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: QueryMiracastDriverInterface
req.alt-loc: Netdispumdddi.h
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
---

# QUERY_MIRACAST_DRIVER_INTERFACE callback



## -description
Called by the operating system to query the Miracast user-mode driver interface, <a href="display.miracast_driver_interface">MIRACAST_DRIVER_INTERFACE</a>.



## -prototype

````
QUERY_MIRACAST_DRIVER_INTERFACE QueryMiracastDriverInterface;

NTSTATUS QueryMiracastDriverInterface(
  _In_  UINT MiracastDriverInterfaceVersion,
  _In_  UINT MiracastDriverInterfaceSize,
  _Out_ VOID *pMiracastDriverInterface
)
{ ... }
````


## -parameters

### -param MiracastDriverInterfaceVersion [in]

The version of the Miracast display interface, supplied by the operating system. 

This version is defined in Netdispumdddi.h as a <b>MIRACAST_DRIVER_INTERFACE_VERSION_XXX</b> value. For Windows 8.1, the value is <b>MIRACAST_DRIVER_INTERFACE_VERSION_1</b>.


### -param MiracastDriverInterfaceSize [in]

The size, supplied by the operating system, of the buffer pointed to by <i>pMiracastDriverInterface</i>.


### -param pMiracastDriverInterface [out]

A pointer to a buffer, supplied by the operating system, that holds the returned Miracast display driver interface, which is a structure of type <a href="display.miracast_driver_interface">MIRACAST_DRIVER_INTERFACE</a>.


## -returns
On success, this function returns <b>STATUS_SUCCESS</b>. Otherwise, the function returns an error code defined in the Ntstatus.h header.


## -remarks
When the Miracast user-mode driver is loaded, the operating system calls the <a href="base.getprocaddress">GetProcAddress</a> function with "QueryMiracastDriverInterface" entered as the function name in the <i>lpProcName</i> parameter.


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 8.1

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2012 R2

</td>
</tr>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Netdispumdddi.h (include Netdispumdddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="base.getprocaddress">GetProcAddress</a>
</dt>
<dt>
<a href="display.miracast_driver_interface">MIRACAST_DRIVER_INTERFACE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20QUERY_MIRACAST_DRIVER_INTERFACE callback function%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

