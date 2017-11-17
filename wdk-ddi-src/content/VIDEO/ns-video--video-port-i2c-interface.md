---
UID: NS.video._VIDEO_PORT_I2C_INTERFACE
title: VIDEO_PORT_I2C_INTERFACE
author: windows-driver-content
description: The VIDEO_PORT_I2C_INTERFACE structure describes the I2C service routines provided by the video port driver.
old-location: display\video_port_i2c_interface.htm
ms.assetid: fcc2679c-9a73-4bd0-ad2d-e7b48df9c7f7
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: video.h
req.include-header: Video.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VIDEO_PORT_I2C_INTERFACE
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
req.irql: See Remarks section.
ms.keywords: VIDEO_PORT_I2C_INTERFACE, VIDEO_PORT_I2C_INTERFACE, *PVIDEO_PORT_I2C_INTERFACE
req.iface: 
req.product: Windows 10 or later.
---

# VIDEO_PORT_I2C_INTERFACE structure



## -description
<p>The VIDEO_PORT_I2C_INTERFACE structure describes the <a href="wdkgloss.i#wdkgloss.inter_integrated_circuit__i2c_#wdkgloss.inter_integrated_circuit__i2c_"><i>I2C</i></a> service routines provided by the video port driver. </p>


## -syntax

````
typedef struct _VIDEO_PORT_I2C_INTERFACE {
  USHORT                 Size;
  USHORT                 Version;
  PVOID                  Context;
  PINTERFACE_REFERENCE   InterfaceReference;
  PINTERFACE_DEREFERENCE InterfaceDereference;
  PI2C_START             I2CStart;
  PI2C_STOP              I2CStop;
  PI2C_WRITE             I2CWrite;
  PI2C_READ              I2CRead;
} VIDEO_PORT_I2C_INTERFACE, *PVIDEO_PORT_I2C_INTERFACE;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Specifies the size in bytes of this structure.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>Specifies the version of the interface to be returned by the miniport driver. The current interface version is defined in <i>video.h</i>, and has the form VIDEO_PORT_I2C_INTERFACE_<i>N</i>.</p>
</dd>

### -field <b>Context</b>

<dd>
<p>Pointer to a miniport driver-defined context for the interface.</p>
</dd>

### -field <b>InterfaceReference</b>

<dd>
<p>Pointer to the video port driver-implemented reference routine for this interface.</p>
</dd>

### -field <b>InterfaceDereference</b>

<dd>
<p>Pointer to the video port driver-implemented dereference routine for this interface.</p>
</dd>

### -field <b>I2CStart</b>

<dd>
<p>Pointer to the video port driver's <a href="https://msdn.microsoft.com/90f0a38d-f50e-4da0-b98f-2f3068f03b2e">I2CStart</a> routine.</p>
</dd>

### -field <b>I2CStop</b>

<dd>
<p>Pointer to the video port driver's <a href="https://msdn.microsoft.com/535e1603-08e3-4ad1-b4e5-f0368b7d3e71">I2CStop</a> routine.</p>
</dd>

### -field <b>I2CWrite</b>

<dd>
<p>Pointer to the video port driver's <a href="https://msdn.microsoft.com/5aaebf38-bc09-4fb5-969e-7b456773d5ac">I2CWrite</a> routine.</p>
</dd>

### -field <b>I2CRead</b>

<dd>
<p>Pointer to the video port driver's <a href="https://msdn.microsoft.com/1418ec29-be67-46af-b6db-0b534ecafb37">I2CRead</a> routine.</p>
</dd>
</dl>

## -remarks
<p>PnP video miniport drivers that can use I²C should fill in the <b>Size</b> and <b>Version</b> members of this structure, and then call <a href="https://msdn.microsoft.com/library/windows/hardware/ff570337">VideoPortQueryServices</a>, which initializes the remaining members of this structure.</p>

## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570337">VideoPortQueryServices</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn895657">INTERFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VIDEO_PORT_I2C_INTERFACE structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
