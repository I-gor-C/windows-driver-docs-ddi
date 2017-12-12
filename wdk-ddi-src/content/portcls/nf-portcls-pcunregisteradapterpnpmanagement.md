---
UID: NF.portcls.PcUnregisterAdapterPnpManagement
title: PcUnregisterAdapterPnpManagement function
author: windows-driver-content
description: The PcUnregisterAdapterPnpManagement function unregisters the audio adapter's PnP management interface from the PortCls class driver. It is used to support PnP rebalance.
old-location: audio\pcunregisteradapterpnpmanagement.htm
old-project: audio
ms.assetid: 51BBE9F6-7661-45A1-8416-9AAA307FCA10
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: PcUnregisterAdapterPnpManagement
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
req.alt-api: PcUnregisterAdapterPnpManagement
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
---

# PcUnregisterAdapterPnpManagement function



## -description
The <b>PcUnregisterAdapterPnpManagement</b> function unregisters the audio adapter's PnP management interface from the PortCls class driver.  It is used to support PnP rebalance. 



## -syntax

````
PORTCLASSAPI NTSTATUS NTAPI PcUnregisterAdapterPnpManagement(
  _In_ PDEVICE_OBJECT DeviceObject
);
````


## -parameters

### -param DeviceObject [in]

Specifies a pointer to a <a href="kernel.device_object">DEVICE_OBJECT</a> structure that represents the functional device object of the adapter.


## -returns
The <b>PcUnregisterAdapterPnpManagement</b>  function returns STATUS_SUCCESS if the function call was successful. Otherwise, it returns the appropriate error code.


## -remarks
The <b>PcUnregisterAdapterPnpManagement</b>  function unregisters a driver's PnP management interface that was registered with PortCls by using the <b>PcUnregisterAdapterPnpManagement</b>  function. 

 This function must only be called if the PnP management interface for the adapter was previously registered with PortCls using <a href="audio.pcregisteradapterpnpmanagement">PcRegisterAdapterPnpManagement</a>.

Portcls uses <a href="audio.pcregisteradapterpnpmanagement">PcRegisterAdapterPnpManagement</a> and <b>PcUnregisterAdapterPnpManagement</b> to support PNP rebalance. 


For more information,  see <a href="https://msdn.microsoft.com/FCAD7F8B-AA9B-430A-BCAF-04E13FA15382">Implement PnP Rebalance for PortCls Audio Drivers</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows 10, version 1511 and later versions of Windows.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Portcls.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.device_object">DEVICE_OBJECT</a>
</dt>
<dt>
<a href="audio.pcregisteradapterpnpmanagement">PcRegisterAdapterPnpManagement</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PcUnregisterAdapterPnpManagement function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

