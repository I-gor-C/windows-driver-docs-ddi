---
UID: NF.ksproxy.IKsPropertySet.Get
title: IKsPropertySet::Get
author: windows-driver-content
description: The Get method retrieves a property identified by a property-set GUID and a property identifier.
old-location: stream\ikspropertyset_get.htm
ms.assetid: 09b131f1-4e09-47f7-89b5-970b8b3e495a
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ksproxy.h
req.include-header: Ksproxy.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IKsPropertySet.Get
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
ms.keywords: IKsPropertySet, Get, IKsPropertySet::Get
req.iface: IKsPropertySet
---

# IKsPropertySet::Get method



## -description
<p>The <b>Get</b> method retrieves a property identified by a property-set GUID and a property identifier.</p>


## -syntax

````
HRESULT Get(
  [in]  REFGUID PropSet,
  [in]  ULONG   Id,
  [in]  LPVOID  InstanceData,
  [in]  ULONG   InstanceLength,
  [out] LPVOID  PropertyData,
  [in]  ULONG   DataLength,
  [out] ULONG   *BytesReturned
);
````


## -parameters
<dl>

### -param <i>PropSet</i> [in]

<dd>
<p>GUID that identifies the property set.</p>
</dd>

### -param <i>Id</i> [in]

<dd>
<p>Identifier of the property within the property set. </p>
</dd>

### -param <i>InstanceData</i> [in]

<dd>
<p>Pointer to instance data for the property. </p>
</dd>

### -param <i>InstanceLength</i> [in]

<dd>
<p>Size, in bytes, of the buffer at <i>InstanceData</i>. </p>
</dd>

### -param <i>PropertyData</i> [out]

<dd>
<p>Pointer to a buffer that receives the value of the property. </p>
</dd>

### -param <i>DataLength</i> [in]

<dd>
<p>Size, in bytes, of the buffer at <i>PropertyData</i>. </p>
</dd>

### -param <i>BytesReturned</i> [out]

<dd>
<p>Pointer to a variable that receives the size, in bytes, of the data that <b>Get</b> stores in the buffer at <i>PropertyData</i>. </p>
</dd>
</dl>

## -returns
<p>Returns NOERROR if successful; otherwise, returns an error code.</p>

## -remarks
<p>To retrieve a property, allocate a buffer, which <b>Get</b> fills with the property. To determine the necessary buffer size, specify <b>NULL</b> for <i>PropertyData</i> and zero for <i>DataLength</i>. The <b>Get</b> method returns the required buffer size in <i>BytesReturned</i>. </p><p class="note">Header files <i>ksproxy.h</i> and <i>dsound.h</i> define similar but incompatible versions of the <b>IKsPropertySet</b> interface. Applications that require the KS proxy module should use the version defined in <i>ksproxy.h</i>. The DirectSound version of <b>IKsPropertySet</b> is described in the DirectSound reference pages in the Microsoft Windows SDK documentation.</p><p class="note">

If an application must include both <i>ksproxy.h</i> and <i>dsound.h</i>, whichever header file the compiler scans first is the one whose definition of <b>IKsPropertySet</b> is used by the compiler.

</p>

<p>To retrieve a property, allocate a buffer, which <b>Get</b> fills with the property. To determine the necessary buffer size, specify <b>NULL</b> for <i>PropertyData</i> and zero for <i>DataLength</i>. The <b>Get</b> method returns the required buffer size in <i>BytesReturned</i>. </p><p class="note">Header files <i>ksproxy.h</i> and <i>dsound.h</i> define similar but incompatible versions of the <b>IKsPropertySet</b> interface. Applications that require the KS proxy module should use the version defined in <i>ksproxy.h</i>. The DirectSound version of <b>IKsPropertySet</b> is described in the DirectSound reference pages in the Microsoft Windows SDK documentation.</p><p class="note">

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
<dt>Ksproxy.h (include Ksproxy.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560721">IKsPropertySet::Set</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsPropertySet::Get method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
