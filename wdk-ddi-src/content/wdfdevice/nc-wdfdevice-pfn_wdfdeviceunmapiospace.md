---
UID: NC:wdfdevice.PFN_WDFDEVICEUNMAPIOSPACE
title: PFN_WDFDEVICEUNMAPIOSPACE function
author: windows-driver-content
description: The WdfDeviceUnmapIoSpace function unmaps a specified range of physical addresses previously mapped by the WdfDeviceMapIoSpace function.
old-location: wdf\wdfdeviceunmapiospace.htm
old-project: wdf
ms.assetid: C8963667-D2FB-4360-A523-33429D6FBF1B
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: PFN_WDFDEVICEUNMAPIOSPACE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 2.0
req.alt-api: WdfDeviceUnmapIoSpace
req.alt-loc: WUDFx02000.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: WUDFx02000.lib
req.dll: WUDFx02000.dll
req.irql: PASSIVE_LEVEL
req.typenames: WDF_DEVICE_SHUTDOWN_FLAGS
req.product: Windows 10 or later.
---

# PFN_WDFDEVICEUNMAPIOSPACE function



## -description
<p class="CCE_Message">[Applies to UMDF only]

The <b>WdfDeviceUnmapIoSpace</b> function unmaps a specified range of physical addresses previously mapped by the <a href="..\wdfdevice\nf-wdfdevice-wdfdevicemapiospace.md">WdfDeviceMapIoSpace</a> function.



## -syntax

````
void WdfDeviceUnmapIoSpace(
  _In_ WDFDEVICE Device,
  _In_ PVOID     PseudoBaseAddress,
  _In_ SIZE_T    NumberOfBytes
);
````


## -parameters

### -param Device [in]

A handle to a framework device object.


### -param PseudoBaseAddress [in]

The address of a location that receives a pointer to the pseudo base address.




### -param NumberOfBytes [in]

Specifies a value greater than zero, indicating the number of bytes to be mapped.


## -returns
This function does not return a value.


## -remarks
This function is the UMDF version 2 equivalent of <a href="https://msdn.microsoft.com/E95AC8E6-222A-4C88-8EBD-6BD7F22B9F18">IWDFDevice3::UnmapIoSpace</a>.

If a driver calls <a href="..\wdfdevice\nf-wdfdevice-wdfdevicemapiospace.md">WdfDeviceMapIoSpace</a> in <a href="..\wdfdevice\nc-wdfdevice-evt_wdf_device_prepare_hardware.md">EvtDevicePrepareHardware</a> callback, it must call <b>WdfDeviceUnmapIoSpace</b> in its <a href="..\wdfdevice\nc-wdfdevice-evt_wdf_device_release_hardware.md">EvtDeviceReleaseHardware</a> callback.




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
Minimum support

</th>
<td width="70%">
Windows 8.1

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>WUDFx02000.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>WUDFx02000.dll</dt>
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
<a href="..\wdfdevice\nf-wdfdevice-wdfdevicemapiospace.md">WdfDeviceMapIoSpace</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/E95AC8E6-222A-4C88-8EBD-6BD7F22B9F18">IWDFDevice3::UnmapIoSpace</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceUnmapIoSpace function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

