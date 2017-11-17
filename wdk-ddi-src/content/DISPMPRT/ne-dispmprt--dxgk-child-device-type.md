---
UID: NE.dispmprt._DXGK_CHILD_DEVICE_TYPE
title: DXGK_CHILD_DEVICE_TYPE
author: windows-driver-content
description: The DXGK_CHILD_DEVICE_TYPE enumeration is used to indicate the type of a child device of the display adapter.
old-location: display\dxgk_child_device_type.htm
ms.assetid: b16ba776-a6b2-46d0-9b6f-18ea17cf4fce
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_CHILD_DEVICE_TYPE
req.alt-loc: dispmprt.h
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
ms.keywords: SYMBOL_INFO_EX, SYMBOL_INFO_EX, *PSYMBOL_INFO_EX
req.iface: IDebugSystemObjects4
---

# DXGK_CHILD_DEVICE_TYPE enumeration



## -description
<p>The DXGK_CHILD_DEVICE_TYPE enumeration is used to indicate the type of a child device of the display adapter.</p>


## -syntax

````
typedef enum _DXGK_CHILD_DEVICE_TYPE { 
  TypeUninitialized,
  TypeVideoOutput,
  TypeOther,
  TypeIntegratedDisplay
} DXGK_CHILD_DEVICE_TYPE, *PDXGK_CHILD_DEVICE_TYPE;
````


## -enum-fields
<dl>

### -field <a id="TypeUninitialized"></a><a id="typeuninitialized"></a><a id="TYPEUNINITIALIZED"></a><b>TypeUninitialized</b>

<dd>
<p>Indicates that a variable of type DXGK_CHILD_DEVICE_TYPE has not yet been assigned a meaningful value.</p>
</dd>

### -field <a id="TypeVideoOutput"></a><a id="typevideooutput"></a><a id="TYPEVIDEOOUTPUT"></a><b>TypeVideoOutput</b>

<dd>
<p>Indicates that the child device is a video output. A video output is the circuitry on the display adapter that supplies a video signal to an external or integrated monitor (or other display device). Note that monitors, integrated LCD panels, and other devices that actually display an image are not considered child devices of the display adapter. </p>
</dd>

### -field <a id="TypeOther"></a><a id="typeother"></a><a id="TYPEOTHER"></a><b>TypeOther</b>

<dd>
<p>Indicates that the child device is not a video output. TV tuners, crossbar switches, and MPEG2 codecs are examples of child devices that are not video outputs.</p>
</dd>

### -field <a id="TypeIntegratedDisplay"></a><a id="typeintegrateddisplay"></a><a id="TYPEINTEGRATEDDISPLAY"></a><b>TypeIntegratedDisplay</b>

<dd>
<p>Type indicating that this target is permanently connected to an integrated display.</p>
</dd>
</dl>

## -remarks
<p>The <b>ChildDeviceType</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561001">DXGK_CHILD_DESCRIPTOR</a> structure is a DXGK_CHILD_DEVICE_TYPE value.</p>

<p>For more information about child devices of display adapters, see <a href="https://msdn.microsoft.com/9fd20e1a-db98-4571-8fc4-6d33fd0e2f16">Child Devices of the Display Adapter</a> and <a href="https://msdn.microsoft.com/3bec2117-aef4-41fc-b88a-0081c7c9fe3d">Enumerating Child Devices of a Display Adapter</a>.</p>

<p>The <b>ChildDeviceType</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561001">DXGK_CHILD_DESCRIPTOR</a> structure is a DXGK_CHILD_DEVICE_TYPE value.</p>

<p>For more information about child devices of display adapters, see <a href="https://msdn.microsoft.com/9fd20e1a-db98-4571-8fc4-6d33fd0e2f16">Child Devices of the Display Adapter</a> and <a href="https://msdn.microsoft.com/3bec2117-aef4-41fc-b88a-0081c7c9fe3d">Enumerating Child Devices of a Display Adapter</a>.</p>

<p>The <b>ChildDeviceType</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561001">DXGK_CHILD_DESCRIPTOR</a> structure is a DXGK_CHILD_DEVICE_TYPE value.</p>

<p>For more information about child devices of display adapters, see <a href="https://msdn.microsoft.com/9fd20e1a-db98-4571-8fc4-6d33fd0e2f16">Child Devices of the Display Adapter</a> and <a href="https://msdn.microsoft.com/3bec2117-aef4-41fc-b88a-0081c7c9fe3d">Enumerating Child Devices of a Display Adapter</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dispmprt.h (include Dispmprt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561001">DXGK_CHILD_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/eb1a0df0-6239-4d82-8477-7dd015f80b6e">DxgkDdiQueryChildRelations</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_CHILD_DEVICE_TYPE enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
