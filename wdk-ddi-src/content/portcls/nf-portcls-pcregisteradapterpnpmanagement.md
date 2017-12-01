---
UID: NF.portcls.PcRegisterAdapterPnpManagement
title: PcRegisterAdapterPnpManagement
author: windows-driver-content
description: The PcRegisterAdapterPnpManagement function registers the adapter's PnP-management interface with the PortCls system driver. It is used to support PnP rebalance.
old-location: audio\pcregisteradapterpnpmanagement.htm
old-project: audio
ms.assetid: DF597216-FB81-466C-871E-5E08C69B78DA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PcRegisterAdapterPnpManagement
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 10, version 1511 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PcRegisterAdapterPnPManagement
req.alt-loc: Portcls.lib,Portcls.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Portcls.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# PcRegisterAdapterPnpManagement function



## -description
<p>The  PcRegisterAdapterPnpManagement function registers the adapter's PnP-management interface with the PortCls system driver.  It is used to support PnP rebalance. </p>


## -syntax

````
NTSTATUS PcRegisterAdapterPnPManagement(
  _In_ PUNKNOWN       pUnknown,
  _In_ PDEVICE_OBJECT DeviceObject
);
````


## -parameters
<dl>

### -param <i>pUnknown</i> [in]

<dd>
<p>Pointer to an adapter driver object's <a href="com.iunknown">IUnknown</a> interface. The PortCls system driver queries this object for its <a href="..\portcls\nn-portcls-iadapterpnpmanagement.md">IAdapterPnpManagement</a> interface.</p>
</dd>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Specifies a pointer to a <a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a> structure that represents the functional device object of the adapter.</p>
</dd>
</dl>

## -returns
<p><b>PcRegisterAdapterPnpManagement</b> returns STATUS_SUCCESS if the call was successful. Otherwise, it returns an appropriate error code.</p>

## -remarks
<p>Portcls uses <b>PcRegisterAdapterPnpManagement</b> and <a href="..\portcls\nf-portcls-pcunregisteradapterpnpmanagement.md">PcUnregisterAdapterPnpManagement</a> to support PNP rebalance.</p>

<p>For more information,  see <a href="NULL">Implement PnP Rebalance for PortCls Audio Drivers</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 10, version 1511 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.lib</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a>
</dt>
<dt>
<a href="..\portcls\nf-portcls-pcunregisteradapterpnpmanagement.md">PcUnregisterAdapterPnpManagement</a>
</dt>
<dt>
<a href="..\portcls\nn-portcls-iadapterpnpmanagement.md">IAdapterPnpManagement</a>
</dt>
<dt>
<a href="NULL">Implement PnP Rebalance for PortCls Audio Drivers</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PcRegisterAdapterPnpManagement function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
