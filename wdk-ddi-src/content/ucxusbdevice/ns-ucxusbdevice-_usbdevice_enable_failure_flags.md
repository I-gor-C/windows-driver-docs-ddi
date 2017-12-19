---
UID: NS.UCXUSBDEVICE._USBDEVICE_ENABLE_FAILURE_FLAGS
title: _USBDEVICE_ENABLE_FAILURE_FLAGS
author: windows-driver-content
description: The flags that are set by the client driver in the EVT_UCX_USBDEVICE_ENABLE callback function. Indicate errors, if any, that might have occurred while enabling the device.
old-location: buses\_usbdevice_enable_failure_flags.htm
old-project: UsbRef
ms.assetid: B239E637-2920-48A5-9F45-D3089140C8A2
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _USBDEVICE_ENABLE_FAILURE_FLAGS, USBDEVICE_ENABLE_FAILURE_FLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucxusbdevice.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBDEVICE_ENABLE_FAILURE_FLAGS
req.alt-loc: ucxusbdevice.h
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
req.product: Windows 10 or later.
---

# _USBDEVICE_ENABLE_FAILURE_FLAGS structure



## -description
The flags that are set by the client driver in the  <a href="..\ucxusbdevice\nc-ucxusbdevice-evt_ucx_usbdevice_enable.md">EVT_UCX_USBDEVICE_ENABLE</a> callback function. Indicate errors, if any, that might have occurred while enabling the device.



## -syntax

````
typedef struct _USBDEVICE_ENABLE_FAILURE_FLAGS {
  ULONG InsufficientHardwareResourcesForDefaultEndpoint  :1;
  ULONG InsufficientHardwareResourcesForDevice  :1;
  ULONG Reserved  :30;
} USBDEVICE_ENABLE_FAILURE_FLAGS, *P_USBDEVICE_ENABLE_FAILURE_FLAGS;
````


## -struct-fields

### -field InsufficientHardwareResourcesForDefaultEndpoint

Insufficient  hardware resources for  transfers to the default endpoint. 


### -field InsufficientHardwareResourcesForDevice

Insufficient hardware resources to enable transfers.


### -field Reserved

Do not use.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ucxusbdevice.h (include Ucxclass.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses._usbdevice_enable">USBDEVICE_ENABLE</a>
</dt>
<dt>
<a href="..\ucxusbdevice\nc-ucxusbdevice-evt_ucx_usbdevice_enable.md">EVT_UCX_USBDEVICE_ENABLE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [UsbRef\buses]:%20USBDEVICE_ENABLE_FAILURE_FLAGS structure%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

