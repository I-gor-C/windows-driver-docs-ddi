---
UID: NS.bdatypes._BDA_TEMPLATE_PIN_JOINT
title: BDA_TEMPLATE_PIN_JOINT
author: windows-driver-content
description: The BDA_TEMPLATE_PIN_JOINT structure describes a joint in a template topology.
old-location: stream\bda_template_pin_joint.htm
ms.assetid: 83df4c9e-7122-4087-9d03-98f2eeed4ec4
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: bdatypes.h
req.include-header: Bdatypes.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BDA_TEMPLATE_PIN_JOINT
req.alt-loc: bdatypes.h
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
ms.keywords: BDA_TEMPLATE_PIN_JOINT, BDA_TEMPLATE_PIN_JOINT, *PBDA_TEMPLATE_PIN_JOINT
req.iface: 
---

# BDA_TEMPLATE_PIN_JOINT structure



## -description
<p>The BDA_TEMPLATE_PIN_JOINT structure describes a joint in a template topology. </p>


## -syntax

````
typedef struct _BDA_TEMPLATE_PIN_JOINT {
  ULONG uliTemplateConnection;
  ULONG ulcInstancesMax;
} BDA_TEMPLATE_PIN_JOINT, *PBDA_TEMPLATE_PIN_JOINT;
````


## -struct-fields
<dl>

### -field <b>uliTemplateConnection</b>

<dd>
<p>Index of an element in a array of template connections (KSTOPOLOGY_CONNECTION or BDA_TEMPLATE_CONNECTION array) that represents the joint.</p>
</dd>

### -field <b>ulcInstancesMax</b>

<dd>
<p>Maximum number of possible instances of the joint in the template topology.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Bdatypes.h (include Bdatypes.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556558">BDA_TEMPLATE_CONNECTION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567148">KSTOPOLOGY_CONNECTION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20BDA_TEMPLATE_PIN_JOINT structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
