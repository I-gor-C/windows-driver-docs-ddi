---
UID: NF:ksproxy.IKsPropertySet.Get
title: IKsPropertySet::Get method
author: windows-driver-content
description: The Get method retrieves a property identified by a property-set GUID and a property identifier.
old-location: stream\ikspropertyset_get.htm
old-project: stream
ms.assetid: 09b131f1-4e09-47f7-89b5-970b8b3e495a
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: Get method [Streaming Media Devices], Get method [Streaming Media Devices], IKsPropertySet interface, Get,IKsPropertySet.Get, IKsPropertySet, IKsPropertySet interface [Streaming Media Devices], Get method, IKsPropertySet::Get, ksproxy/IKsPropertySet::Get, ksproxy_d5ef4576-b05f-466d-8d87-094d97f83e10.xml, stream.ikspropertyset_get
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: ksproxy.h
req.include-header: Ksproxy.h, Dsound.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: ksproxy.h
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	ksproxy.h
api_name:
-	IKsPropertySet.Get
product: Windows
targetos: Windows
req.typenames: PIPE_STATE
---


# Get method
The <b>Get</b> method retrieves a property identified by a property-set GUID and a property identifier.

## Syntax

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

## Parameters

`PropSet`



`Id`



`InstanceData`



`InstanceLength`



`PropertyData`



`DataLength`



`BytesReturned`




## Return Value

Returns NOERROR if successful; otherwise, returns an error code.

## Remarks

To retrieve a property, allocate a buffer, which <b>Get</b> fills with the property. To determine the necessary buffer size, specify <b>NULL</b> for <i>PropertyData</i> and zero for <i>DataLength</i>. The <b>Get</b> method returns the required buffer size in <i>BytesReturned</i>. 

<div class="alert"><b>Warning</b>  <p class="note">Header files <i>ksproxy.h</i> and <i>dsound.h</i> define similar but incompatible versions of the <b>IKsPropertySet</b> interface. Applications that require the KS proxy module should use the version defined in <i>ksproxy.h</i>. The DirectSound version of <b>IKsPropertySet</b> is described in the DirectSound reference pages in the Microsoft Windows SDK documentation.

<p class="note">

If an application must include both <i>ksproxy.h</i> and <i>dsound.h</i>, whichever header file the compiler scans first is the one whose definition of <b>IKsPropertySet</b> is used by the compiler.



</div>
<div> </div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | ksproxy.h (include Ksproxy.h, Dsound.h) |
| **Library** | ksproxy.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff560721">IKsPropertySet::Set</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsPropertySet::Get method%20 RELEASE:%20(2/23/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>