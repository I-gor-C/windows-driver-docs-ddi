---
UID: NF.video.VideoPortInitialize
title: VideoPortInitialize
author: windows-driver-content
description: The VideoPortInitialize function performs part of the miniport driver initialization, allocating system resources for the miniport driver.
old-location: display\videoportinitialize.htm
old-project: display
ms.assetid: cc0da962-beeb-4035-a68e-e5b856cd5d9b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VideoPortInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VideoPortInitialize
req.alt-loc: Videoprt.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Videoprt.lib
req.dll: Videoprt.sys
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# VideoPortInitialize function



## -description
<p>The <b>VideoPortInitialize</b> function performs part of the miniport driver initialization, allocating system resources for the miniport driver.</p>


## -syntax

````
ULONG VideoPortInitialize(
   PVOID                         Argument1,
   PVOID                         Argument2,
   PVIDEO_HW_INITIALIZATION_DATA HwInitializationData,
   PVOID                         HwContext
);
````


## -parameters
<dl>

### -param <i>Argument1</i> 

<dd>
<p>A pointer with which the operating system called <a href="https://msdn.microsoft.com/library/windows/hardware/ff556159">DriverEntry of Video Miniport Driver</a>.</p>
</dd>

### -param <i>Argument2</i> 

<dd>
<p>A second pointer with which the operating system called <b>DriverEntry</b>.</p>
</dd>

### -param <i>HwInitializationData</i> 

<dd>
<p>Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570505">VIDEO_HW_INITIALIZATION_DATA</a> structure on the stack. The miniport driver's <b>DriverEntry</b> routine zero-initialized this structure and then filled it in with driver-specific configuration information describing a video adapter that the miniport driver can support.</p>
</dd>

### -param <i>HwContext</i> 

<dd>
<p>Must be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p><b>VideoPortInitialize</b> returns the final status of the initialization operation. </p>

## -remarks
<p>Every video miniport driver must call <b>VideoPortInitialize</b> from its <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> function. <b>DriverEntry</b> can call <b>VideoPortInitialize</b> only after it has first zero-initialized and then set up the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570505">VIDEO_HW_INITIALIZATION_DATA</a> structure. <b>VideoPortInitialize</b> can be called only from a miniport driver's <b>DriverEntry</b> function.</p>

<p>The <b>VideoPortInitialize</b> function:</p>

<p>Checks the validity of the miniport driver's VIDEO_HW_INITIALIZATION_DATA specifications.</p>

<p>Allocates memory for and zero-initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff570531">VIDEO_PORT_CONFIG_INFO</a> structure.</p>

<p>Fills in as much adapter configuration information as it can in VIDEO_PORT_CONFIG_INFO.</p>

<p>Fills in some of the public members of the device object created by the system to represent the graphics adapter. The video port driver manages the device objects, therefore, the miniport driver need not be concerned with device object details.</p>

<p>Allocates memory for, and zero-initializes the device extension of, the device object. A <i>device extension </i>is each miniport driver's primary and only global storage area for adapter-specific state information. The miniport driver specifies the size of the device extension in the <b>HwDeviceExtensionSize</b> member of VIDEO_HW_INITIALIZATION_DATA. The video port driver passes this device extension to most of the miniport driver functions that it calls.</p>

<p>Collects and stores pertinent information in the device extension.</p>

<p>The miniport driver's <b>DriverEntry</b> routine propagates the value returned by <b>VideoPortInitialize</b> back to its caller. Miniport drivers should not use this return value. </p>

<p>Every video miniport driver must call <b>VideoPortInitialize</b> from its <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> function. <b>DriverEntry</b> can call <b>VideoPortInitialize</b> only after it has first zero-initialized and then set up the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570505">VIDEO_HW_INITIALIZATION_DATA</a> structure. <b>VideoPortInitialize</b> can be called only from a miniport driver's <b>DriverEntry</b> function.</p>

<p>The <b>VideoPortInitialize</b> function:</p>

<p>Checks the validity of the miniport driver's VIDEO_HW_INITIALIZATION_DATA specifications.</p>

<p>Allocates memory for and zero-initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff570531">VIDEO_PORT_CONFIG_INFO</a> structure.</p>

<p>Fills in as much adapter configuration information as it can in VIDEO_PORT_CONFIG_INFO.</p>

<p>Fills in some of the public members of the device object created by the system to represent the graphics adapter. The video port driver manages the device objects, therefore, the miniport driver need not be concerned with device object details.</p>

<p>Allocates memory for, and zero-initializes the device extension of, the device object. A <i>device extension </i>is each miniport driver's primary and only global storage area for adapter-specific state information. The miniport driver specifies the size of the device extension in the <b>HwDeviceExtensionSize</b> member of VIDEO_HW_INITIALIZATION_DATA. The video port driver passes this device extension to most of the miniport driver functions that it calls.</p>

<p>Collects and stores pertinent information in the device extension.</p>

<p>The miniport driver's <b>DriverEntry</b> routine propagates the value returned by <b>VideoPortInitialize</b> back to its caller. Miniport drivers should not use this return value. </p>

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
<p>Available in Windows 2000 and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Video.h (include Video.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Videoprt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Videoprt.sys</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556159">DriverEntry of Video Miniport Driver</a>
</dt>
<dt>
<a href="..\video\nc-video-pvideo-hw-find-adapter.md">HwVidFindAdapter</a>
</dt>
<dt>
<a href="..\video\nc-video-pvideo-hw-initialize.md">HwVidInitialize</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570505">VIDEO_HW_INITIALIZATION_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570531">VIDEO_PORT_CONFIG_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570493">VideoPortZeroMemory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortInitialize function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
