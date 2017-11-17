---
UID: NS.ksmedia.PKSPROPERTY_CAMERACONTROL_NODE_FOCAL_LENGTH_S
title: PKSPROPERTY_CAMERACONTROL_NODE_FOCAL_LENGTH_S
author: windows-driver-content
description: The KSPROPERTY_CAMERACONTROL_NODE_FOCAL_LENGTH_S structure returns node-specific data requested using the KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH property.
old-location: stream\ksproperty_cameracontrol_node_focal_length_s.htm
ms.assetid: 7562f84d-aac2-48b6-bae2-518d1f58f71f
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSPROPERTY_CAMERACONTROL_NODE_FOCAL_LENGTH_S
req.alt-loc: ksmedia.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: PKSPROPERTY_CAMERACONTROL_NODE_FOCAL_LENGTH_S, KSPROPERTY_CAMERACONTROL_NODE_FOCAL_LENGTH_S, *PKSPROPERTY_CAMERACONTROL_NODE_FOCAL_LENGTH_S
req.iface: 
---

# PKSPROPERTY_CAMERACONTROL_NODE_FOCAL_LENGTH_S structure



## -description
<p>The KSPROPERTY_CAMERACONTROL_NODE_FOCAL_LENGTH_S structure returns node-specific data requested using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564406">KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH</a> property.</p>


## -syntax

````
typedef struct {
  KSNODEPROPERTY NodeProperty;
  LONG           lOcularFocalLength;
  LONG           lObjectiveFocalLengthMin;
  LONG           lObjectiveFocalLengthMax;
} KSPROPERTY_CAMERACONTROL_NODE_FOCAL_LENGTH_S, *PKSPROPERTY_CAMERACONTROL_NODE_FOCAL_LENGTH_S;
````


## -struct-fields
<dl>

### -field <b>NodeProperty</b>

<dd>
<p>Specifies both the target node and the property to <i>get</i>. This member is an initialized structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff537143">KSNODEPROPERTY</a>.</p>
</dd>

### -field <b>lOcularFocalLength</b>

<dd>
<p>Specifies a value of type LONG containing the focal length of the lens closest to the camera user.</p>
</dd>

### -field <b>lObjectiveFocalLengthMin</b>

<dd>
<p>Specifies a value of type LONG containing the minimum focal length of the lens closest to the camera subject.</p>
</dd>

### -field <b>lObjectiveFocalLengthMax</b>

<dd>
<p>Specifies a value of type LONG containing the maximum focal length of the lens closest to the camera subject.</p>
</dd>
</dl>

## -remarks
<p>If the camera has only one lens, these values can be used to represent zoom ratios. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff564406">KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h (include Ksmedia.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567802">PROPSETID_VIDCAP_CAMERACONTROL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564406">KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564408">KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_CAMERACONTROL_NODE_FOCAL_LENGTH_S structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
