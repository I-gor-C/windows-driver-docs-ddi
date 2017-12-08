---
UID: NS.hbapiwmi._GetBindingCapability_IN
title: GetBindingCapability_IN
author: windows-driver-content
description: The GetBindingCapability_IN structure is used by a WMI client to deliver the input parameter data of the GetBindingCapability WMI method to the HBA miniport driver.
old-location: storage\getbindingcapability_in.htm
old-project: storage
ms.assetid: cd4046db-f9f5-4c9e-8886-29504c727f67
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: GetBindingCapability_IN, GetBindingCapability_IN, *PGetBindingCapability_IN
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hbapiwmi.h
req.include-header: Hbapiwmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GetBindingCapability_IN
req.alt-loc: hbapiwmi.h
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
req.iface: 
---

# GetBindingCapability_IN structure



## -description
<p>The GetBindingCapability_IN structure is used by a WMI client to deliver the input parameter data of the <a href="storage.getbindingcapability">GetBindingCapability</a> WMI method to the HBA miniport driver.</p>


## -syntax

````
typedef struct _GetBindingCapability_IN {
  UCHAR PortWWN[8];
} GetBindingCapability_IN, *PGetBindingCapability_IN;
````


## -struct-fields
<dl>

### -field PortWWN

<dd>
<p>Contains a worldwide name that indicates the port whose persistent bindings are to be retrieved. </p>
</dd>
</dl>

## -remarks
<p>The WMI tool suite generates a declaration of the GetBindingCapability_IN structure in <i>Hbapiwmi.h </i>when it compiles the <a href="storage.msfc_hbafcpinfo_wmi_class">MSFC_HBAFCPInfo WMI Class</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hbapiwmi.h (include Hbapiwmi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.getbindingcapability">GetBindingCapability</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20GetBindingCapability_IN structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
