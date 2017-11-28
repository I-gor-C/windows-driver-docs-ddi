---
UID: NC.ursdevice.EVT_URS_SET_ROLE
title: EVT_URS_SET_ROLE
author: windows-driver-content
description: The URS class extension invokes this event callback when it requires the client driver to change the role of the controller.
old-location: buses\evt_urs_set_role.htm
old-project: usbref
ms.assetid: 287B674F-9692-47FA-AB92-F101270F7FC4
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UPSWaitForStateChange
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ursdevice.h
req.include-header: Urscx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 
req.alt-api: PFN_URS_SET_ROLE
req.alt-loc: ursdevice.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# EVT_URS_SET_ROLE callback



## -description
<p>The URS class extension invokes this event callback when it requires the client driver to change the role of the controller.</p>


## -prototype

````
EVT_URS_SET_ROLE EvtUrsSetRole;

NTSTATUS EvtUrsSetRole(
  _In_ WDFDEVICE Device,
  _In_ URS_ROLE  Role
)
{ ... }

typedef EVT_URS_SET_ROLE PFN_URS_SET_ROLE;
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to the framework device object that the client driver retrieved in the previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>.</p>
</dd>

### -param <i>Role</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/mt628024">URS_ROLE</a> type value that indicates the role to set for the controller device.</p>
</dd>
</dl>

## -returns
<p>If the operation is successful, the callback function must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise it must return a status value for which NT_SUCCESS(status) equals FALSE.</p>

## -remarks
<p> To register the client driver's implementation of the event callback the driver must set the  <b>EvtUrsSetRole</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/mt628020">URS_CONFIG</a> to a function pointer of the implementation method and then call the <a href="https://msdn.microsoft.com/library/windows/hardware/mt628012">UrsDeviceInitialize</a> method by passing the populated structure. The driver must call the method after it creates the framework device object for the controller. </p>

<p> To register the client driver's implementation of the event callback the driver must set the  <b>EvtUrsSetRole</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/mt628020">URS_CONFIG</a> to a function pointer of the implementation method and then call the <a href="https://msdn.microsoft.com/library/windows/hardware/mt628012">UrsDeviceInitialize</a> method by passing the populated structure. The driver must call the method after it creates the framework device object for the controller. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.15</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ursdevice.h (include Urscx.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt628012">UrsDeviceInitialize</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20EVT_URS_SET_ROLE callback function%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
