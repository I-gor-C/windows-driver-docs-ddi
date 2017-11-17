---
UID: NS.hbapiwmi._GetPortAttributesByWWN_IN
title: GetPortAttributesByWWN_IN
author: windows-driver-content
description: The GetPortAttributesByWWN_IN structure is used by a WMI client to deliver input parameter data to the GetPortAttributesByWWN WMI method.
old-location: storage\getportattributesbywwn_in.htm
ms.assetid: 2b189ece-6c49-42e2-8ef2-b3db516fc844
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: hbapiwmi.h
req.include-header: Hbapiwmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GetPortAttributesByWWN_IN
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
ms.keywords: GetPortAttributesByWWN_IN, GetPortAttributesByWWN_IN, *PGetPortAttributesByWWN_IN
req.iface: 
---

# GetPortAttributesByWWN_IN structure



## -description
<p>The GetPortAttributesByWWN_IN structure is used by a WMI client to deliver input parameter data to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554965">GetPortAttributesByWWN</a> WMI method. </p>


## -syntax

````
typedef struct _GetPortAttributesByWWN_IN {
  UCHAR wwn[8];
} GetPortAttributesByWWN_IN, *PGetPortAttributesByWWN_IN;
````


## -struct-fields
<dl>

### -field <b>wwn</b>

<dd>
<p>Contains a worldwide name that identifies a port of type FC_Port.</p>
</dd>
</dl>

## -remarks
<p>The WMI tool suite generates a declaration of the GetPortAttributesByWWN_IN structure in <i>Hbapiwmi.h </i>when it compiles the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562506">MSFC_HBAAdapterMethods WMI Class</a>.</p>

<p>For a definition of FC_Port and a discussion of worldwide names, see the T11 committee's specification for <i>Fibre Channel HBA API</i> (FC-HBA).</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554965">GetPortAttributesByWWN</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20GetPortAttributesByWWN_IN structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
