---
UID : NS:d4drvif._DOT4_DC_CREATE_DATA
title : "_DOT4_DC_CREATE_DATA"
author : windows-driver-content
description : Defines the DOT4_DC_CREATE_DATA construct.
old-location : print\dot4_dc_create_data.htm
old-project : print
ms.assetid : 9C21732B-0AB1-4F3E-8F3D-F0B12007920A
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : d4drvif/DOT4_DC_CREATE_DATA, PDOT4_DC_CREATE_DATA, DOT4_DC_CREATE_DATA, d4drvif/PDOT4_DC_CREATE_DATA, print.dot4_dc_create_data, _DOT4_DC_CREATE_DATA, DOT4_DC_CREATE_DATA structure [Print Devices], PDOT4_DC_CREATE_DATA structure pointer [Print Devices], *PDOT4_DC_CREATE_DATA
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d4drvif.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PDOT4_DC_CREATE_DATA, DOT4_DC_CREATE_DATA"
---

# _DOT4_DC_CREATE_DATA structure
Defines the <b>DOT4_DC_CREATE_DATA</b> construct.

## Syntax
````
typedef struct _DOT4_DC_CREATE_DATA {
  unsigned char bPsid;
  CHAR          pServiceName[MAX_SERVICE_LENGTH + 1];
  unsigned char bType;
  ULONG         ulBufferSize;
  USHORT        usMaxHtoPPacketSize;
  USHORT        usMaxPtoHPacketSize;
  unsigned char bHsid;
} DOT4_DC_CREATE_DATA, *PDOT4_DC_CREATE_DATA;
````

## Members


`bHsid`

Specifies the host socket ID returned.

`bPsid`

Specifies this or the service name sent.

`bType`

Specifies the type, stream or packet, of channels on the socket.

`pServiceName`

Describes the <b>CHAR</b>  member <b>pServiceName</b>.

`ulBufferSize`

Specifies the size of the read buffer for channels on socket.

`usMaxHtoPPacketSize`

Describes the <b>USHORT</b> member <b>usMaxHtoPPacketSize</b>.

`usMaxPtoHPacketSize`

Describes the <b>USHORT</b> member <b>usMaxPtoHPacketSize</b>.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d4drvif.h |