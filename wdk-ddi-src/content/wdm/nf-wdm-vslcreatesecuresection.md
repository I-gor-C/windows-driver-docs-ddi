---
UID: NF:wdm.VslCreateSecureSection
title: VslCreateSecureSection function
author: windows-driver-content
description: This material is not yet available. This placeholder topic is provided as an example of documentation that may be included in a later release.
old-location: kernel\vslcreatesecuresection.htm
old-project: kernel
ms.assetid: 005e738e-dc38-404a-bd74-8aa342f8186b
ms.author: windowsdriverdev
ms.date: 3/1/2018
ms.keywords: VslCreateSecureSection, VslCreateSecureSection function [Kernel-Mode Driver Architecture], kernel.vslcreatesecuresection, wdm/VslCreateSecureSection
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Wdm.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
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
topic_type:
-	kbSyntax
api_type:
-	<TBD>
api_location:
-
api_name:
-	VslCreateSecureSection
product: Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# VslCreateSecureSection function
This material is not yet available. This placeholder topic is provided as an example of documentation that may be included in a later release.

## Syntax

````
NTSTATUS  VslCreateSecureSection(
   PHANDLE   Handle,
   PEPROCESS TargetProcess,
   PMDL      Mdl,
   ULONG     DevicePageProtection,
   ULONG     Attributes
);
````

## Parameters

`Handle`

TBD

`TargetProcess`

TBD

`Mdl`

TBD

`DevicePageProtection`

TBD

`Attributes`

TBD


## Return Value

}


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows Server 2016 |
| **Target Platform** | Windows |
| **Header** | wdm.h (include Wdm.h, Wdm.h) |