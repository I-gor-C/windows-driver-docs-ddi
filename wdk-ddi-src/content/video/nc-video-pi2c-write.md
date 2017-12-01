---
UID: NC.video.PI2C_WRITE
title: PI2C_WRITE
author: windows-driver-content
description: The I2CWrite function writes data over the I2C channel.
old-location: display\i2cwrite.htm
old-project: display
ms.assetid: 5aaebf38-bc09-4fb5-969e-7b456773d5ac
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VHF_CONFIG, VHF_CONFIG, *PVHF_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: I2CWrite
req.alt-loc: video.h
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

# PI2C_WRITE callback



## -description
<p>The <i>I2CWrite</i> function writes data over the <a href="wdkgloss.i#wdkgloss.inter_integrated_circuit__i2c_#wdkgloss.inter_integrated_circuit__i2c_"><i>I2C</i></a> channel.</p>


## -prototype

````
PI2C_WRITE I2CWrite;

BOOLEAN I2CWrite(
  _In_ PVOID          HwDeviceExtension,
  _In_ PI2C_CALLBACKS I2CCallbacks,
  _In_ PUCHAR         Buffer,
  _In_ ULONG          Length
)
{ ... }
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the miniport driver's per-adapter device extension.</p>
</dd>

### -param <i>I2CCallbacks</i> [in]

<dd>
<p>Pointer to an <a href="..\video\ns-video--i2c-callbacks.md">I2C_CALLBACKS</a> structure, containing pointers to miniport driver-defined functions that read and write data and clock lines.</p>
</dd>

### -param <i>Buffer</i> [in]

<dd>
<p>Pointer to the data to be written.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Specifies the number of bytes to be written.</p>
</dd>
</dl>

## -returns
<p><i>I2CWrite</i> returns <b>TRUE</b> if the data was successfully written, and <b>FALSE</b> otherwise.</p>

## -remarks
<p>The video port implements this function, which can be accessed through a pointer in the <a href="..\video\ns-video--video-port-i2c-interface.md">VIDEO_PORT_I2C_INTERFACE</a> structure. </p>

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
<a href="..\video\ns-video--video-port-i2c-interface.md">VIDEO_PORT_I2C_INTERFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PI2C_WRITE callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
