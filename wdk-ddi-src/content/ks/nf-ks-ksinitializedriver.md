---
UID: NF.ks.KsInitializeDriver
title: KsInitializeDriver function
author: windows-driver-content
description: The KsInitializeDriver function initializes the driver object of an AVStream minidriver.
old-location: stream\ksinitializedriver.htm
old-project: stream
ms.assetid: 5a77e59f-ce64-4ff2-ac95-c9062cef20d2
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: KsInitializeDriver
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsInitializeDriver
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: PASSIVE_LEVEL
---

# KsInitializeDriver function



## -description
The<b> KsInitializeDriver </b>function initializes the driver object of an AVStream minidriver.



## -syntax

````
NTSTATUS KsInitializeDriver(
  _In_           PDRIVER_OBJECT      DriverObject,
  _In_           PUNICODE_STRING     RegistryPath,
  _In_opt_ const KSDEVICE_DESCRIPTOR *Descriptor
);
````


## -parameters

### -param DriverObject [in]

A pointer to the <a href="kernel.driver_object">DRIVER_OBJECT</a> structure for the AVStream driver being initialized. Minidrivers that call <b>KsInitializeDriver</b> should use the driver object passed to <b>DriverEntry</b> by the operating system.


### -param RegistryPath [in]

A pointer to a Unicode string containing the registry path string passed into the minidriver's <b>DriverEntry</b> function by the operating system.


### -param Descriptor [in, optional]

A pointer to a <a href="stream.ksdevice_descriptor">KSDEVICE_DESCRIPTOR</a> structure that specifies the characteristics of the device being initialized. If this pointer is <b>NULL</b>, a device is created with default characteristics and no associated filter factories.


## -returns
<b>KsInitializeDriver</b> returns STATUS_SUCCESS or an appropriate error code as returned by <a href="kernel.iocreatedevice">IoCreateDevice</a> or internal AVStream device initialization routines.  


## -remarks
This function is typically called from <b>DriverEntry</b>. If the minidriver passes in a device descriptor, AVStream creates a device with the specified characteristics at <b>AddDevice</b> time. Minidrivers that perform device initialization themselves do not necessarily need to call <b>KsInitializeDriver</b>.  For more information, see <a href="https://msdn.microsoft.com/666d6efb-93ec-43f3-87c5-ea1a3983bfd0">Initializing an AVStream Minidriver</a>.


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
Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
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
<a href="stream.ksdevice_dispatch">KSDEVICE_DISPATCH</a>
</dt>
<dt>
<a href="stream.ksfilter_descriptor">KSFILTER_DESCRIPTOR</a>
</dt>
<dt>
<a href="stream.ksinitializedevice">KsInitializeDevice</a>
</dt>
<dt>
<a href="stream.ksdevice_descriptor">KSDEVICE_DESCRIPTOR</a>
</dt>
<dt>
<a href="kernel.iocreatedevice">IoCreateDevice</a>
</dt>
<dt>
<a href="stream.driverentry_of_avstream">DriverEntry of AVStream</a>
</dt>
<dt>
<a href="kernel.driver_object">DRIVER_OBJECT</a>
</dt>
<dt>
<a href="kernel.device_object">DEVICE_OBJECT</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsInitializeDriver function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

