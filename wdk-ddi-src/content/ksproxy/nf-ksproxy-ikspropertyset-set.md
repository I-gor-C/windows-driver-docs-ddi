---
UID: NF.ksproxy.IKsPropertySet.Set
title: IKsPropertySet::Set
author: windows-driver-content
description: The Set method sets a property identified by a property-set GUID and a property identifier.
old-location: stream\ikspropertyset_set.htm
old-project: stream
ms.assetid: 959a78e2-b5c8-47b0-97b1-52d9565a6dab
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IKsPropertySet, Set, IKsPropertySet::Set
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ksproxy.h
req.include-header: Ksproxy.h, Ksproxy.h, Dsound.h, Ksproxy.h, Ksproxy.h, Dsound.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IKsPropertySet.Set
req.alt-loc: ksproxy.h
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
req.iface: IKsPropertySet
---

# IKsPropertySet::Set method



## -description
<p>The <b>Set</b> method sets a property identified by a property-set GUID and a property identifier.</p>


## -syntax

````
HRESULT Set(
  [in] REFGUID PropSet,
  [in] ULONG   Id,
  [in] LPVOID  InstanceData,
  [in] ULONG   InstanceLength,
  [in] LPVOID  PropertyData,
  [in] ULONG   DataLength
);
````


## -parameters
<dl>

### -param PropSet [in]

<dd>
<p>GUID that identifies the property set.</p>
</dd>

### -param Id [in]

<dd>
<p>Identifier of the property within the property set. </p>
</dd>

### -param InstanceData [in]

<dd>
<p>Pointer to instance data for the property. </p>
</dd>

### -param InstanceLength [in]

<dd>
<p>Size, in bytes, of the buffer at <i>InstanceData</i>. </p>
</dd>

### -param PropertyData [in]

<dd>
<p>Pointer to a buffer that contains the value of the property to set. </p>
</dd>

### -param DataLength [in]

<dd>
<p>Size, in bytes, of the buffer at <i>PropertyData</i>. </p>
</dd>
</dl>

## -returns
<p>Returns NOERROR if successful; otherwise, returns an error code.</p>

## -remarks
<p class="note">Header files <i>ksproxy.h</i> and <i>dsound.h</i> define similar but incompatible versions of the <b>IKsPropertySet</b> interface. Applications that require the KS proxy module should use the version defined in <i>ksproxy.h</i>. The DirectSound version of <b>IKsPropertySet</b> is described in the DirectSound reference pages in the Microsoft Windows SDK documentation.</p><p class="note">

If an application must include both <i>ksproxy.h</i> and <i>dsound.h</i>, whichever header file the compiler scans first is the one whose definition of <b>IKsPropertySet</b> is used by the compiler.

</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksproxy.h (include Ksproxy.h, Ksproxy.h, Dsound.h, Ksproxy.h, Ksproxy.h, or Dsound.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="stream.ikspropertyset_get">IKsPropertySet::Get</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsPropertySet::Set method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
