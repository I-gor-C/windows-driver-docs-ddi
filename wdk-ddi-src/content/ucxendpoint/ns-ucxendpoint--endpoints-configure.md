---
UID: NS.ucxendpoint._ENDPOINTS_CONFIGURE
title: ENDPOINTS_CONFIGURE
author: windows-driver-content
description: Describes endpoints to enable or disable endpoints. This structure is passed by UCX in the EVT_UCX_USBDEVICE_ENDPOINTS_CONFIGURE callback function.
old-location: buses\_endpoints_configure.htm
old-project: usbref
ms.assetid: C24B7D85-AEA9-43B3-9BEE-262CAA255834
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: ENDPOINTS_CONFIGURE, ENDPOINTS_CONFIGURE, *PENDPOINTS_CONFIGURE
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
req.alt-api: ENDPOINTS_CONFIGURE
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

# ENDPOINTS_CONFIGURE structure



## -description
<p>Describes   endpoints to enable or disable endpoints. This structure is passed by UCX in the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187842">EVT_UCX_USBDEVICE_ENDPOINTS_CONFIGURE</a>  callback function.</p>


## -syntax

````
typedef struct _ENDPOINTS_CONFIGURE {
#if _cplusplus
  USBDEVICE_MGMT_HEADER             Header;
#else 
  USBDEVICE_MGMT_HEADER             ;
#endif 
  ULONG                             EndpointsToEnableCount;
  UCXENDPOINT                       *EndpointsToEnable;
  ULONG                             EndpointsToDisableCount;
  UCXENDPOINT                       *EndpointsToDisable;
  ULONG                             EndpointsEnabledAndUnchangedCount;
  UCXENDPOINT                       *EndpointsEnabledAndUnchanged;
  ENDPOINTS_CONFIGURE_FAILURE_FLAGS FailureFlags;
  ULONG                             ExitLatencyDelta;
  UCHAR                             ConfigurationValue;
  UCHAR                             InterfaceNumber;
  UCHAR                             AlternateSetting;
} ENDPOINTS_CONFIGURE, *P_ENDPOINTS_CONFIGURE;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/mt188075">USBDEVICE_MGMT_HEADER</a> structure that stores handles to the USB hub or device whose endpoints.</p>
</dd>

### -field <b>EndpointsToEnableCount</b>

<dd>
<p>The number of endpoints to configure.</p>
</dd>

### -field <b>EndpointsToEnable</b>

<dd>
<p>A pointer to the first endpoint handle in the array of endpoints to  enable.</p>
</dd>

### -field <b>EndpointsToDisableCount</b>

<dd>
<p>The number of endpoints to configure.</p>
</dd>

### -field <b>EndpointsToDisable</b>

<dd>
<p>A pointer to the first endpoint handle in the array of endpoints to  enable.</p>
</dd>

### -field <b>EndpointsEnabledAndUnchangedCount</b>

<dd>
<p>The number of endpoints that were enabled and unchanged.</p>
</dd>

### -field <b>EndpointsEnabledAndUnchanged</b>

<dd>
<p>A pointer to the first endpoint handle in the array of endpoints that have not been changed.</p>
</dd>

### -field <b>FailureFlags</b>

<dd>
<p>The errors, if any, that might occur when attempting to configure endpoints for the USB device or hub.</p>
</dd>

### -field <b>ExitLatencyDelta</b>

<dd>
<p>The Exit Latency Delta (ELD) value. For more information see section 4.6.6.1 of the eXtensible Host Controller Interface specification.</p>
</dd>

### -field <b>ConfigurationValue</b>

<dd>
<p>The configuration number of the USB configuration that contains the endpoints. </p>
</dd>

### -field <b>InterfaceNumber</b>

<dd>
<p>The interface number of the USB interface that contains the endpoints. </p>
</dd>

### -field <b>AlternateSetting</b>

<dd>
<p>The setting number of the alternate setting that contains the endpoints. </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt187842">EVT_UCX_USBDEVICE_ENDPOINTS_CONFIGURE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20ENDPOINTS_CONFIGURE structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
