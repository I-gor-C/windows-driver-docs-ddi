---
UID: NC:wdfdevice.PFN_WDFWDMDEVICEGETWDFDEVICEHANDLE
title: PFN_WDFWDMDEVICEGETWDFDEVICEHANDLE function
author: windows-driver-content
description: The WdfWdmDeviceGetWdfDeviceHandle method returns a handle to the framework device object that is associated with a specified WDM device object.
old-location: wdf\wdfwdmdevicegetwdfdevicehandle.htm
old-project: wdf
ms.assetid: 8083af10-1b35-4600-b409-e895d35f7ccc
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: PFN_WDFWDMDEVICEGETWDFDEVICEHANDLE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfWdmDeviceGetWdfDeviceHandle
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.typenames: WDF_DEVICE_SHUTDOWN_FLAGS
req.product: Windows 10 or later.
---

# PFN_WDFWDMDEVICEGETWDFDEVICEHANDLE function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfWdmDeviceGetWdfDeviceHandle</b> method returns a handle to the framework device object that is associated with a specified WDM device object.



## -syntax

````
WDFDEVICE WdfWdmDeviceGetWdfDeviceHandle(
  _In_ PDEVICE_OBJECT DeviceObject
);
````


## -parameters

### -param DeviceObject [in]

A pointer to a WDM <a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a> structure that the calling driver created.


## -returns
If the specified WDM device object is valid, <b>WdfWdmDeviceGetWdfDeviceHandle</b> returns a handle to the associated framework device object. Otherwise, the method returns <b>NULL</b>.


## -remarks
The WDM DEVICE_OBJECT structure that the driver specifies for the <i>DeviceObject</i> parameter must represent a device object that the calling driver created. For example, the structure cannot represent any of the WDM device objects that the driver specified in a previous call to <a href="..\wdfminiport\nf-wdfminiport-wdfdeviceminiportcreate.md">WdfDeviceMiniportCreate</a>.

The following code example obtains a handle to the framework device object that is associated with a WDM device object that the calling driver created.


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
Minimum KMDF version

</th>
<td width="70%">
1.0

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
<dt>Wdf01000.sys (see <a href="https://msdn.microsoft.com/51db6f3c-45cb-46a7-9dd4-2bab67893fea">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;=DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfminiport\nf-wdfminiport-wdfdeviceminiportcreate.md">WdfDeviceMiniportCreate</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfWdmDeviceGetWdfDeviceHandle method%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

