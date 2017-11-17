---
UID: NC.wdm.PCI_SET_ACS
title: PCI_SET_ACS
author: windows-driver-content
description: 
ms.assetid: 9da3f488-708b-42c1-b468-7f49e051e785
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# PCI_SET_ACS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCI_SET_ACS PciSetAcs; 

// Definition

NTSTATUS PciSetAcs 
(
	PVOID Context
	PCI_ACS_BIT EnableSourceValidation
	PCI_ACS_BIT EnableTranslationBlocking
	PCI_ACS_BIT EnableP2PRequestRedirect
	PCI_ACS_BIT EnableCompletionRedirect
	PCI_ACS_BIT EnableUpstreamForwarding
	PCI_ACS_BIT EnableEgressControl
	PCI_ACS_BIT EnableDirectTranslatedP2P
)
{...}

PCI_SET_ACS PPCI_SET_ACS


```

## -parameters

### -param Context: 
### -param EnableSourceValidation: 
### -param EnableTranslationBlocking: 
### -param EnableP2PRequestRedirect: 
### -param EnableCompletionRedirect: 
### -param EnableUpstreamForwarding: 
### -param EnableEgressControl: 
### -param EnableDirectTranslatedP2P: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also