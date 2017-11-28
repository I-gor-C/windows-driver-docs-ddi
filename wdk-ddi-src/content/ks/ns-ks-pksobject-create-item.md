---
UID: NS.ks.PKSOBJECT_CREATE_ITEM
title: PKSOBJECT_CREATE_ITEM
author: windows-driver-content
description: The KSOBJECT_CREATE_ITEM structure is used to look up the string passed to a create request.
old-location: stream\ksobject_create_item.htm
old-project: stream
ms.assetid: 9c047a7c-cdfc-47e1-beae-f8f326c187ee
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PKSOBJECT_CREATE_ITEM, KSOBJECT_CREATE_ITEM, *PKSOBJECT_CREATE_ITEM
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSOBJECT_CREATE_ITEM
req.alt-loc: ks.h
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

# PKSOBJECT_CREATE_ITEM structure



## -description
<p>The KSOBJECT_CREATE_ITEM structure is used to look up the string passed to a create request.</p>


## -syntax

````
typedef struct {
  PDRIVER_DISPATCH     Create;
  PVOID                Context;
  UNICODE_STRING       ObjectClass;
  PSECURITY_DESCRIPTOR SecurityDescriptor;
  ULONG                Flags;
} KSOBJECT_CREATE_ITEM, *PKSOBJECT_CREATE_ITEM;
````


## -struct-fields
<dl>

### -field <b>Create</b>

<dd>
<p>Contains the create dispatch function for this particular base object class. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff544174">DRIVER_OBJECT</a> for the signature of this function type.</p>
</dd>

### -field <b>Context</b>

<dd>
<p>Points to a buffer that can be used to store object type-specific context information. Additional information is in the Remarks section below.</p>
</dd>

### -field <b>ObjectClass</b>

<dd>
<p>Points to a Unicode string that identifies the object class. This is the string that was used to register with PnP for a particular class of object supported by this device.</p>
</dd>

### -field <b>SecurityDescriptor</b>

<dd>
<p>Contains a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563689">SECURITY_DESCRIPTOR</a> for this type of object, otherwise <b>NULL</b>. If security is used, this must be freed when the object type is no longer used. This must use pool memory, and cannot be shared, as it may be replaced. If this is modified, the <b>Flags</b> element is updated. Optional.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Specifies the request type. Flags can have the values listed in the following table.</p>
<table>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>KSCREATE_ITEM_SECURITYCHANGED</p>
</td>
<td>
<p>Indicates that the security descriptor on this object type has been changed and should be persisted.</p>
</td>
</tr>
<tr>
<td>
<p>KSCREATE_ITEM_WILDCARD</p>
</td>
<td>
<p>Indicates that this create item represents a wild card that is used for any create requests that do not match any other create items. The ordering of the wild card entry in the list of create items is irrelevant. Only a single wild card entry is valid on any list of create items.</p>
</td>
</tr>
<tr>
<td>
<p>KSCREATE_ITEM_NOPARAMETERS</p>
</td>
<td>
<p>Indicates that this create item does not allow any parameters to be passed, and fails if any are found. Normally, create parameters are passed on to the create handler. This cannot be used with a wild card flag.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks
<p>A pointer to the KSOBJECT_CREATE_ITEM structure is placed in the <b>DriverContext</b> member of <b>Irp-&gt;Tail.Overlay</b> before the object is created. You can access this pointer by using the KSCREATE_ITEM_IRP_STORAGE macro. This macro and related macros are included in <i>ks.h</i>.</p>

<p>The minidriver might retrieve this pointer when creating a new object to examine the <b>Context</b> field.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560958">KsAllocateDeviceHeader</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560972">KsAllocateObjectHeader</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562531">KsFilterFactoryAddCreateItem</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSOBJECT_CREATE_ITEM structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
