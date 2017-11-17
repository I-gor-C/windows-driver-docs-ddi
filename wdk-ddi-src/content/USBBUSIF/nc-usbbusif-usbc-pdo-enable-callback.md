---
UID: NC.usbbusif.USBC_PDO_ENABLE_CALLBACK
title: USBC_PDO_ENABLE_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 1659fc9c-0321-4e7e-b316-beee98e96856
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: usbbusif.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.irql: 
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# USBC_PDO_ENABLE_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

USBC_PDO_ENABLE_CALLBACK UsbcPdoEnableCallback; 

// Definition

BOOLEAN UsbcPdoEnableCallback 
(
	PVOID Context
	USHORT FirstInterfaceNumber
	USHORT NumberOfInterfaces
	UCHAR FunctionClass
	UCHAR FunctionSubClass
	UCHAR FunctionProtocol
)
{...}

USBC_PDO_ENABLE_CALLBACK 


```

## -parameters

### -param Context: 
### -param FirstInterfaceNumber: 
### -param NumberOfInterfaces: 
### -param FunctionClass: 
### -param FunctionSubClass: 
### -param FunctionProtocol: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also