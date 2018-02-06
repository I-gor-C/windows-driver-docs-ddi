---
UID: NF:ks.KsSetInformationFile
title: KsSetInformationFile function
author: windows-driver-content
description: The KsSetInformationFile function performs an information set against the specified file object. The function attempts to use FastIoDispatch if possible, or it generates an information set against the device object.
old-location: stream\kssetinformationfile.htm
old-project: stream
ms.assetid: 878c6565-99f9-4f45-abba-ba4ece5b5743
ms.author: windowsdriverdev
ms.date: 1/9/2018
ms.keywords: ks/KsSetInformationFile, ksfunc_338e56fe-b32d-4c9e-920f-9a5af1c5fdf3.xml, KsSetInformationFile, KsSetInformationFile function [Streaming Media Devices], stream.kssetinformationfile
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
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
req.lib: Ks.lib
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	LibDef
apilocation:
-	Ks.lib
-	Ks.dll
apiname:
-	KsSetInformationFile
product: Windows
targetos: Windows
req.typenames: 
---


# KsSetInformationFile function
The <b>KsSetInformationFile</b> function performs an information set against the specified file object. The function attempts to use <b>FastIoDispatch</b> if possible, or it generates an information set against the device object.

## Syntax

````
NTSTATUS KsSetInformationFile(
  _In_ PFILE_OBJECT           FileObject,
  _In_ PVOID                  FileInformation,
  _In_ ULONG                  Length,
  _In_ FILE_INFORMATION_CLASS FileInformationClass
);
````

## Parameters

`FileObject`

Specifies the file object to set the standard information on.

`FileInformation`

Indicates the place in which to put the file information. The file information is assumed to be a valid or probed address.

`Length`

Specifies the correct length of the <i>FileInformation</i> buffer.

`FileInformationClass`

Specifies the class of information being set.


## Return Value

The <b>KsSetInformationFile</b> function returns STATUS_SUCCESS if successful, or if unsuccessful it returns a set error.

## Remarks

The <b>KsSetInformationFile</b> function should be used only when the set would result in an actual request to the underlying driver, not including complex operations that require additional parameters to be sent to the driver such as rename, deletion, and completion. For example, <b>FilePositionInformation</b> would not generate such a request and should not be used. It assumes the caller is serializing access to the file for operations against a FO_SYNCHRONOUS_IO file object.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | ks.h (include Ks.h) |
| **Library** | Ks.lib |