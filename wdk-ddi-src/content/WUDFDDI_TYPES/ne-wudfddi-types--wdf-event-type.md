---
UID: NE.wudfddi_types._WDF_EVENT_TYPE
title: WDF_EVENT_TYPE
author: windows-driver-content
description: The WDF_EVENT_TYPE enumeration specifies.
old-location: wdf\wdf_event_type.htm
ms.assetid: DC6353BB-98C0-4647-9180-F099CD95348E
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfddi_types.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.alt-api: WDF_EVENT_TYPE
req.alt-loc: wdfdevice.h,wudfddi_types.h
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
ms.keywords: WRITE_REGISTER_USHORT
req.iface: 
req.product: Windows 10 or later.
---

# WDF_EVENT_TYPE enumeration



## -description
<p class="CCE_Message">[Applies to UMDF only]</p>
<p>The <b>WDF_EVENT_TYPE</b> enumeration specifies  types of events about which a driver can notify a registered application.</p>


## -syntax

````
typedef enum _WDF_EVENT_TYPE { 
  WdfEventReserved   = 0,
  WdfEventBroadcast  = 1,
  WdfEventMaximum    = 2
} WDF_EVENT_TYPE;
````


## -enum-fields
<dl>

### -field <a id="WdfEventReserved"></a><a id="wdfeventreserved"></a><a id="WDFEVENTRESERVED"></a><b>WdfEventReserved</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="WdfEventBroadcast"></a><a id="wdfeventbroadcast"></a><a id="WDFEVENTBROADCAST"></a><b>WdfEventBroadcast</b>

<dd>
<p>In the current version of UMDF, the driver must specify <b>WdfEventBroadcast</b>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn265606">WdfDevicePostEvent</a>.</p>
</dd>

### -field <a id="WdfEventMaximum"></a><a id="wdfeventmaximum"></a><a id="WDFEVENTMAXIMUM"></a><b>WdfEventMaximum</b>

<dd>
<p>Reserved for system use.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum support</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.11</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h); </dt>
<dt>Wudfddi_types.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265606">WdfDevicePostEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558835">IWDFDevice::PostEvent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_EVENT_TYPE enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
