---
UID : NF:wdfcollection.WdfCollectionGetFirstItem
title : WdfCollectionGetFirstItem function
author : windows-driver-content
description : The WdfCollectionGetFirstItem method returns a handle to the first object that is in an object collection.
old-location : wdf\wdfcollectiongetfirstitem.htm
old-project : wdf
ms.assetid : 4884de4d-6e5f-4c9f-bd49-2fc58481e9c6
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : WdfCollectionGetFirstItem, kmdf.wdfcollectiongetfirstitem, PFN_WDFCOLLECTIONGETFIRSTITEM, DFCollectionObjectRef_1a816492-f120-48f9-9c10-88f71947008c.xml, WdfCollectionGetFirstItem method, wdf.wdfcollectiongetfirstitem, wdfcollection/WdfCollectionGetFirstItem
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : wdfcollection.h
req.include-header : Wdf.h
req.target-type : Universal
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 1.0
req.umdf-ver : 2.0
req.ddi-compliance : DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll : 
req.irql : <= DISPATCH_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : WDF_CHILD_RETRIEVE_INFO, *PWDF_CHILD_RETRIEVE_INFO
req.product : Windows 10 or later.
---


# WdfCollectionGetFirstItem function
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfCollectionGetFirstItem</b> method returns a handle to the first object that is in an object collection.

## Syntax

````
WDFOBJECT WdfCollectionGetFirstItem(
  _In_ WDFCOLLECTION Collection
);
````

## Parameters

`Collection`

A handle to a collection object.


## Return Value

<b>WdfCollectionGetFirstItem</b> returns a handle to the object that is currently at the front of the specified collection's list of objects, or <b>NULL</b> if the list is empty.

A bug check occurs if the driver supplies an invalid object handle.

## Remarks

For more information about object collections, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/framework-object-collections">Framework Object Collections</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfcollection.h (include Wdf.h) |
| **Library** |  |
| **IRQL** | <= DISPATCH_LEVEL |
| **DDI compliance rules** | DriverCreate, KmdfIrql, KmdfIrql2 |

## See Also

<a href="..\wdfcollection\nf-wdfcollection-wdfcollectiongetlastitem.md">WdfCollectionGetLastItem</a>

<a href="..\wdfcollection\nf-wdfcollection-wdfcollectiongetitem.md">WdfCollectionGetItem</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfCollectionGetFirstItem method%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>