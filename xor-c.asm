	.file	"xor.c"
	.text
	.section	.rodata.str1.8,"aMS",@progbits,1
	.align 8
.LC0:
	.string	"Usage: %s <input> <output> <key>\n"
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC1:
	.string	"rb"
.LC2:
	.string	"wb"
.LC3:
	.string	"Error opening file"
.LC4:
	.string	"Error: Key cannot be empty\n"
	.section	.text.unlikely,"ax",@progbits
.LCOLDB5:
	.section	.text.startup,"ax",@progbits
.LHOTB5:
	.p2align 4
	.globl	main
	.type	main, @function
main:
.LFB53:
	.cfi_startproc
	endbr64
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	subq	$4096, %rsp
	.cfi_def_cfa_offset 4152
	orq	$0, (%rsp)
	subq	$24, %rsp
	.cfi_def_cfa_offset 4176
	movq	%fs:40, %rax
	movq	%rax, 4104(%rsp)
	xorl	%eax, %eax
	movq	%rsi, %rbx
	cmpl	$4, %edi
	je	.L2
	movq	(%rsi), %rcx
	movq	stderr(%rip), %rdi
	leaq	.LC0(%rip), %rdx
	movl	$2, %esi
	call	__fprintf_chk@PLT
.L3:
	movl	$1, %eax
	.p2align 4,,10
	.p2align 3
.L1:
	movq	4104(%rsp), %rdx
	subq	%fs:40, %rdx
	jne	.L16
	addq	$4120, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 56
	popq	%rbx
	.cfi_def_cfa_offset 48
	popq	%rbp
	.cfi_def_cfa_offset 40
	popq	%r12
	.cfi_def_cfa_offset 32
	popq	%r13
	.cfi_def_cfa_offset 24
	popq	%r14
	.cfi_def_cfa_offset 16
	popq	%r15
	.cfi_def_cfa_offset 8
	ret
.L2:
	.cfi_restore_state
	movq	8(%rsi), %rdi
	leaq	.LC1(%rip), %rsi
	call	fopen@PLT
	movq	16(%rbx), %rdi
	leaq	.LC2(%rip), %rsi
	movq	%rax, %rbp
	call	fopen@PLT
	movq	%rax, %r12
	testq	%rbp, %rbp
	je	.L12
	testq	%rax, %rax
	je	.L12
	movq	24(%rbx), %r15
	movq	%r15, %rdi
	call	strlen@PLT
	movq	%rax, %r14
	testq	%rax, %rax
	je	.L17
	xorl	%r13d, %r13d
	movq	%rsp, %rbx
	.p2align 4,,10
	.p2align 3
.L7:
	movq	%rbx, %rdi
	movq	%rbp, %rcx
	movl	$4096, %edx
	movl	$1, %esi
	call	fread@PLT
	movq	%rax, %rdi
	testq	%rax, %rax
	je	.L9
	movq	%rbx, %rcx
	leaq	(%rbx,%rax), %rsi
	.p2align 4,,10
	.p2align 3
.L8:
	movzbl	(%r15,%r13), %edx
	leaq	1(%r13), %rax
	xorb	%dl, (%rcx)
	xorl	%edx, %edx
	divq	%r14
	addq	$1, %rcx
	movq	%rdx, %r13
	cmpq	%rsi, %rcx
	jne	.L8
	movq	%rdi, %rdx
	movq	%r12, %rcx
	movl	$1, %esi
	movq	%rbx, %rdi
	call	fwrite@PLT
	jmp	.L7
.L9:
	movq	%rbp, %rdi
	call	fclose@PLT
	movq	%r12, %rdi
	call	fclose@PLT
	xorl	%eax, %eax
	jmp	.L1
.L17:
	movq	stderr(%rip), %rcx
	movl	$27, %edx
	movl	$1, %esi
	leaq	.LC4(%rip), %rdi
	call	fwrite@PLT
	jmp	.L3
.L16:
	call	__stack_chk_fail@PLT
	.cfi_endproc
	.section	.text.unlikely
	.cfi_startproc
	.type	main.cold, @function
main.cold:
.LFSB53:
.L12:
	.cfi_def_cfa_offset 4176
	.cfi_offset 3, -56
	.cfi_offset 6, -48
	.cfi_offset 12, -40
	.cfi_offset 13, -32
	.cfi_offset 14, -24
	.cfi_offset 15, -16
	leaq	.LC3(%rip), %rdi
	call	perror@PLT
	jmp	.L3
	.cfi_endproc
.LFE53:
	.section	.text.startup
	.size	main, .-main
	.section	.text.unlikely
	.size	main.cold, .-main.cold
.LCOLDE5:
	.section	.text.startup
.LHOTE5:
	.ident	"GCC: (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	1f - 0f
	.long	4f - 1f
	.long	5
0:
	.string	"GNU"
1:
	.align 8
	.long	0xc0000002
	.long	3f - 2f
2:
	.long	0x3
3:
	.align 8
4:
