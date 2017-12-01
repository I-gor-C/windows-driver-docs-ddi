---
UID: NF.ndis.NdisIMCancelInitializeDeviceInstance
title: NdisIMCancelInitializeDeviceInstance
author: windows-driver-content
description: The NdisIMCancelInitializeDeviceInstance function cancels a preceding call to the NdisIMInitializeDeviceInstanceEx function.
old-location: netvista\ndisimcancelinitializedeviceinstance.htm
old-project: netvista
ms.assetid: 809ffee1-b087-4bf0-ba8a-1ac0b2d02f2f
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisIMCancelInitializeDeviceInstance
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see       NdisIMCancelInitializeDeviceInstance (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers   (see       NdisIMCancelInitializeDeviceInstance (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisIMCancelInitializeDeviceInstance
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_IM_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# NdisIMCancelInitializeDeviceInstance function



## -description
<p>The 
  <b>NdisIMCancelInitializeDeviceInstance</b> function cancels a preceding call to the 
  <a href="..\ndis\nf-ndis-ndisiminitializedeviceinstanceex.md">
  NdisIMInitializeDeviceInstanceEx</a> function.</p>


## -syntax

````
NDIS_STATUS NdisIMCancelInitializeDeviceInstance(
  _In_ NDIS_HANDLE  DriverHandle,
  _In_ PNDIS_STRING DeviceInstance
);
````


## -parameters
<dl>

### -param <i>DriverHandle</i> [in]

<dd>
<p>The miniport driver handle that the 
     <a href="..\ndis\nf-ndis-ndismregisterminiportdriver.md">
     NdisMRegisterMiniportDriver</a> function returned at the 
     <i>NdisMiniportDriverHandle</i> parameter.</p>
</dd>

### -param <i>DeviceInstance</i> [in]

<dd>
<p>A pointer to an NDIS_STRING type that describes a caller-initialized counted string in the
     system-default character set. The string contains the name of the registry key in which the driver
     stores information about a virtual miniport and, possibly, binding-specific information. For Microsoft
     Windows 2000 and later drivers, this string contains Unicode characters. That is, for Windows 2000 and
     later, NDIS defines the NDIS_STRING type as a 
     <a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a> type.</p>
</dd>
</dl>

## -returns
<p><b>NdisIMCancelInitializeDeviceInstance</b> returns NDIS_STATUS_SUCCESS if it canceled the preceding call
     to 
     <b>NdisIMInitializeDeviceInstanceEx</b>. Otherwise, it returns NDIS_STATUS_FAILURE if there is no way to
     stop the initialization operation for the virtual miniport.</p>

## -remarks
<p>An intermediate driver calls the 
    <a href="..\ndis\nf-ndis-ndisiminitializedeviceinstanceex.md">
    NdisIMInitializeDeviceInstanceEx</a> function to initiate the initialization operation for a virtual
    miniports.Before NDIS calls the driver's 
    <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> function, the
    driver can call 
    <b>NdisIMCancelInitializeDeviceInstance</b> to cancel the initialization operation. For example, if an
    underlying driver that the intermediate driver requires for normal operation is removed, the intermediate
    driver can cancel the initialization for any virtual miniports that are associated with the removed
    driver.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/c942a9ce-e604-4578-b051-48a9bd2f265f">
   NdisIMCancelInitializeDeviceInstance (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers
   (see 
   <b>
   NdisIMCancelInitializeDeviceInstance (NDIS 5.1)</b>) in Windows XP.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.ndis_irql_im_function">Irql_IM_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisiminitializedeviceinstanceex.md">
   NdisIMInitializeDeviceInstanceEx</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismregisterminiportdriver.md">NdisMRegisterMiniportDriver</a>
</dt>
<dt>
<a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisIMCancelInitializeDeviceInstance function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
