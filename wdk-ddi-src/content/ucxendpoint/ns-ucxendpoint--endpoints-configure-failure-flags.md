---
UID: NS.ucxendpoint._ENDPOINTS_CONFIGURE_FAILURE_FLAGS
title: ENDPOINTS_CONFIGURE_FAILURE_FLAGS
author: windows-driver-content
description: This structure provides failure flags to indicate errors, if any, that might have occurred during a request to an EVT_UCX_USBDEVICE_ENDPOINTS_CONFIGURE callback function.
old-location: buses\_endpoints_configure_failure_flags.htm
old-project: usbref
ms.assetid: D605A20B-3747-458E-BA9D-F723F884F130
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: ENDPOINTS_CONFIGURE_FAILURE_FLAGS, ENDPOINTS_CONFIGURE_FAILURE_FLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucxendpoint.h
req.include-header: Ucxclass.h, Ucxendpoint.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ENDPOINTS_CONFIGURE_FAILURE_FLAGS
req.alt-loc: ucxendpoint.h
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
req.iface: 
req.product: Windows 10 or later.
---

# ENDPOINTS_CONFIGURE_FAILURE_FLAGS structure



## -description
<p>This structure provides failure flags to indicate errors, if any, that might have occurred during a request to an <a href="..\ucxusbdevice\nc-ucxusbdevice-evt-ucx-usbdevice-endpoints-configure.md">EVT_UCX_USBDEVICE_ENDPOINTS_CONFIGURE</a> callback function.</p>


## -syntax

````
typedef struct _ENDPOINTS_CONFIGURE_FAILURE_FLAGS {
  ULONG InsufficientBandwidth  :1;
  ULONG InsufficientHardwareResourcesForEndpoints  :1;
  ULONG MaxExitLatencyTooLarge  :1;
  ULONG Reserved  :29;
} ENDPOINTS_CONFIGURE_FAILURE_FLAGS, *P_ENDPOINTS_CONFIGURE_FAILURE_FLAGS;
````


## -struct-fields
<dl>

### -field InsufficientBandwidth

<dd>
<p>Insufficient bandwidth to configure the specified endpoints.</p>
</dd>

### -field InsufficientHardwareResourcesForEndpoints

<dd>
<p>Insufficient hardware resources to configure the specified endpoints.</p>
</dd>

### -field MaxExitLatencyTooLarge

<dd>
<p>The maximum exit latency is too large to configure the specified endpoints.</p>
</dd>

### -field Reserved

<dd>
<p>Do not use.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ucxendpoint.h (include Ucxclass.h or Ucxendpoint.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ucxendpoint\ns-ucxendpoint--endpoints-configure.md">ENDPOINTS_CONFIGURE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20ENDPOINTS_CONFIGURE_FAILURE_FLAGS structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
