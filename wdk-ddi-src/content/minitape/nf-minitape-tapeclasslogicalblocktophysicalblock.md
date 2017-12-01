---
UID: NF.minitape.TapeClassLogicalBlockToPhysicalBlock
title: TapeClassLogicalBlockToPhysicalBlock
author: windows-driver-content
description: The TapeClassLogicalBlockToPhysicalBlock routine translates a pseudological block address to a physical block address. This routine is for SCSI-1 devices.
old-location: storage\tapeclasslogicalblocktophysicalblock.htm
old-project: storage
ms.assetid: 4ad11a15-ba72-4921-a00a-6d3bfb443b51
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: TapeClassLogicalBlockToPhysicalBlock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: minitape.h
req.include-header: Minitape.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TapeClassLogicalBlockToPhysicalBlock
req.alt-loc: Tape.lib,Tape.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Tape.lib
req.dll: 
req.irql: 
req.iface: 
---

# TapeClassLogicalBlockToPhysicalBlock function



## -description
<p>The <b>TapeClassLogicalBlockToPhysicalBlock</b> routine translates a pseudological block address to a physical block address. This routine is for SCSI-1 devices.</p>


## -syntax

````
TAPE_PHYS_POSITION TapeClassLogicalBlockToPhysicalBlock(
  _In_ UCHAR   DensityCode,
  _In_ ULONG   LogicalBlockAddress,
  _In_ ULONG   BlockLength,
  _In_ BOOLEAN FromBOT
);
````


## -parameters
<dl>

### -param <i>DensityCode</i> [in]

<dd>
<p>Specifies the tape media density code. This routine supports tapes with the following density codes: QIC_24, QIC_120, QIC_150, QIC_525, QIC_1000, QIC_2GB, QIC_1350, and QIC_2100.</p>
</dd>

### -param <i>LogicalBlockAddress</i> [in]

<dd>
<p>Specifies a pseudological block address.</p>
</dd>

### -param <i>BlockLength</i> [in]

<dd>
<p>Specifies the logical block size, in bytes.</p>
</dd>

### -param <i>FromBOT</i> [in]

<dd>
<p><b>TRUE</b> indicates that the physical block calculation should start at the beginning of the tape and account for the physical device header. <b>FALSE</b> indicates that the tape has two partitions, that the block address is on the directory partition, and therefore no physical device header needs to be factored into the calculation.</p>
</dd>
</dl>

## -returns
<p><b>TapeClassLogicalBlockToPhysicalBlock</b> returns a structure containing the physical block address:
      </p>

<p>typedef struct _TAPE_PHYS_POSITION {</p>

<p>ULONG SeekBlockAddress;</p>

<p>ULONG SpaceBlockCount;</p>

<p>} TAPE_PHYS_POSITION, PTAPE_PHYS_POSITION;</p>

## -remarks
<p>A tape miniclass driver calls <b>TapeClassLogicalBlockToPhysicalBlock</b> to translate a logical block address from an application to a physical block address for a tape device. <b>TapeClassLogicalBlockToPhysicalBlock</b> is not necessary for SCSI-2 or later drivers because devices that comply with SCSI-2 or later standards support logical block addressing.</p>

<p>To position a tape to the physical block address returned by this routine, a tape miniclass driver issues two SCSI commands: a LOCATE command to position the tape to the <b>SeekBlockAddress</b>, and then a SPACE command to advance the tape <b>SpaceBlockCount</b>. The <b>SpaceBlockCount</b> value is necessary if the pseudological blocks on the tape are smaller than the physical blocks; in that case, the logical block boundary might not align with a physical block boundary.</p>

<p>If a tape miniclass driver calls this routine with an unsupported tape density code, <b>TapeClassLogicalBlockToPhysicalBlock</b> does not perform any translation. It returns the logical block address in <b>SeekBlockAddress</b> and returns zero in <b>SpaceBlockCount</b>.</p>

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
<dt>Minitape.h (include Minitape.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Tape.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\minitape\nf-minitape-tapeclassphysicalblocktologicalblock.md">TapeClassPhysicalBlockToLogicalBlock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20TapeClassLogicalBlockToPhysicalBlock routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
