# Git undoing
* Git 작업 되돌리기
1. Working Directory 작업 단계
   * `git restore {파일 이름}`
   * git 2.23.0 버전 이전에는 git checkout -- {파일 이름}
     * 버전 체크 : git --version
   * 수정한 파일을 수정 전(직전 커밋)으로 되돌리기
   * 이미 버전 관리가 되고 있는 파일만 되돌리기 가능
   * 이 방법으로 되돌렸을 때 `해당 내용을 복원할 수 없음`
* 연습
  * mkdir git-practice
  * ls 
  * cd git-practice
  * git init
  * touch test.md
  * echo Hello > test.md
  * cat test.md
  * git add .
  * git status
  * git commit -m 'commit 01'
  * echo World! >> test.md
  * cat test.md
  * git status
  * git restore test.md
  * cat test.md

  * echo World! >> test.md
  * cat test.md
  * git status
  * git stash
  * cat test.md
  * git stash apply
  * cat test.md
  * git stash
  * git log


2. Staging Area 작업 단계
   * git add를 잘못한 경우
   * working directory로 되돌리기
   * root-commit 여부에 따라
     * 없는 경우 : `git rm --cached {파일 이름}`
       * 한 번도 커밋을 안 한 경우
       * 이미 git에서 관리하고 있는 파일을 더이상 사용하지 않을 때
         * 커밋까지 한 경우에서 사용하고자 하지 않을 떄 사용 => untracked 상태가 됨 ( 새로운 파일과 같음 )
       * -- 없으면 파일 자체가 삭제되므로 주의할 것
     * 있는 경우 : `git restore --staged {파일 이름}`
       * git 저장소에 커밋이 하나라도 있는 경우

* 연습
  * touch rm_test.md
  * echo Hello > rm_test.md
  * git status
  * git add
  * git status    => staging area에 올라온 상태
  * git rm --cached rm_test.md
  * git status    => staging area에서 내려온 상태

  * git add    => test.md만 add 하기 다른 파일은 삭제
  * git restore --staged test.md   => 1번에서 commit 진행했음
  * git status    => staging area에서 내려온 상태

3. Repository 작업 단계
   * `git commit --amend`
   * 팀 단위로 작업시 사용 자제
   * 커밋을 완료한 파일을 staging area로 되돌리기
   * staging area에 새로 올라온 내용이
     * `없다면, 직전 커밋의 메시지만 수정`
     * `있다면, 직전 커밋을 덮어쓰기`
   * 이전 커밋을 완전히 고쳐서 새 커밋으로 변경하므로, 이전 커밋은 일어나지 않은 일이 되며 히스토리에도 남지 않음을 주의
* Vim 사용
  * 입력 모드 i
  * 명령 모드 esc
    * 저장 및 종료 :wq
    * 강제 종료 :q!

* 연습
  * git restore test.md  
  * git stauts   => working area, staging area 비우기
  * git commit --amend
  * i 눌러서 입력 모드로 변환 후 수정할 커밋 메세지 작성 => esc 눌러서 명령 모드로 변환 후 종료 명령어 작성 엔터
  * git log   => commit hash 값 변경 확인, 수정된 커밋 메시지 확인
  * 커밋 메시지 수정하지 않고도 가능

  * touch a.txt
  * git add a.txt
  * git commit -m 'add a'
  * git log
  * touch b.txt
  * git add b.txt
  * git commit --amend     => 커밋된 a.txt를 staging area로 내린 뒤 b.txt와 함께 커밋
  * i => add a, b로 수정 => esc => :wq
  * git log --oneline

--------
# Git reset & revert
* 특정 시간으로 되돌리기 (기록의 유무 차이)
* Git reset
  * 프로젝트를 특정 커밋 상태로 되돌림
  * `되돌리는 특정 커밋 이후로 쌓았던 커밋들은 전부 사라짐`
  * `git reset [옵션] {커밋 ID}`
    * 옵션 
      * `--soft` : 커밋 이후의 파일들은 staging area로 돌려놓음
      * `--mixed` : 커밋 이후의 파일들은 working directory로 돌려놓음 
      * `--hard` : 커밋 이후의 파일들은 모두 working directory에서 `삭제` (기존의 untracked 파일은 남아있음)
        * 복구 가능 : `git reflog`
          * reset하기 전의 커밋 내역을 모두 조회 가능
          * 해당 커밋으로 reset하면 hard 옵션으로 삭제된 파일도 복구 가능
    * 커밋 ID : 되돌아가고 싶은 시점의 커밋 ID (git log 찍어서 볼 수 있는 커밋 hash 값)

* 연습
  * touch reset_test.md
  * git add .
  * git commit -m 'add reset test'
  * git log --oneline   => 커밋한거 세개 만들기
  * git reset --soft HEAD~1
  * git status
  * git log --oneline

  * git commit -m 'add reset test'
  * git reset --mixed 09c81af
  * git log --oneline
  * git status

  * git add .
  * git commit -m 'add reset test'
  * git log --oneline
  * git reset --hard HEAD~1
  * git log --oneline
  * git reflog
  * git reset --hard 09c81af
  * ls

* Git revert
  * 과거를 없었던 일로 만드는 행위로, 이전 커밋을 취소한 다음 새로운 커밋을 생성
  * `git revert {커밋 ID}`
    * 커밋 ID : 취소하고 싶은 커밋 ID
  * reset VS revert
    * reset은 커밋 내역을 삭제 / revert는 새로운 커밋을 생성
    * revert는 github를 이용해 협업할 때, 커밋 내역의 차이로 인한 충돌 방지 가능
    * `git reset 커밋ID` 이라고 작성하면 커밋ID 라는 커밋으로  되돌린다
    * `git revert 커밋ID` 이라고 작성하면 커밋ID 라는 커밋 한개를 취소한다
      * 커밋ID 라는 커밋이 취소되었다는 내용의 새로운 커밋을 생성

* 연습
  * git log --oneline
  * git revert 커밋ID    => 어떤 이유로 취소하는지 이유 작성
  * ls   => 파일 목록에서 사라짐
  * git log --oneline   => 기록은 사라지지 않고, revert했다는 기록이 추가됨

--------
# Git branch & merge
* Git branch
  * Branch는 나뭇가지라는 뜻으로, 여러 갈래로 작업 공간을 나누어 독립적으로 작업할 수 있도록 도와주는 Git의 도구
  * 장점
    * 브랜치는 독립 공간을 형성하기 때문에 원본(master)에 대해 안전함
    * 하나의 작업은 하나의 브랜치로 나누어 진행되므로 체계적인 개발이 가능함
    * Git은 브랜치를 만드는 속도가 굉장히 빠르고, 적은 용량을 소모함
  * 명령어
    * `git branch` : 로컬 저장소의 브랜치 목록 확인
    * `git branch -r` : 원격 저장소의 브랜치 목록 확인
    * `git branch {브랜치 이름}` : 새로운 브랜치 생성
    * `git branch {브랜치 이름} {커밋 ID}` : 특정 커밋 기준으로 브랜치 생성
    * `git branch -d {브랜치 이름}` : 병합된 브랜치만 삭제 가능
    * `git branch -D {브랜치 이름}` : 강제 삭제

* git switch
  * 현재 브랜치에서 다른 브랜치로 이동하는 명령어
  * `git switch {브랜치 이름}` : 다른 브랜치로 이동
  * `git switch -c {브랜치 이름}` : 브랜치를 새로 생성 및 이동
  * `git switch -c {브랜치 이름} {커밋 ID}` : 특정 커밋 기준으로 브랜치 생성 및 이동
  * switch 하기 전에, 해당 브랜치의 변경 사항을 반드시 커밋해야함
  * 다른 브랜치에서 파일을 만들고 커밋하지 않은 상태에서 switch를 하면 브랜치를 이동했음에도 불구하고 해당 파일이 그대로 남아있게 됨

* `git log` or `cat .git/HEAD`  => 현재 HEAD가 어떤 브랜치를 가리키는지 알 수 있음
* `git log --oneline --all` / `git log --oneline --all --graph`

* Git merge
  * 분기된 브랜치들을 하나로 합치는 명령어
  * master 브랜치가 상용이므로, 주로 master 브랜치에 병합
  * `git merge {합칠 브랜치 이름}`
    * 병합하기 전에 `메인 브랜치로 switch 해야함`
    * 병합에는 세 종류가 존재
      * Fast-Forward : 마치 빨리감기처럼 브랜치가 가리키는 커밋을 앞으로 이동시키는 방법
      * 3-way Merge : 각 브랜치의 커밋 두 개와 공통 조상 하나를 사용하여 병합하는 방법
      * Merge Conflict 
        * 두 브랜치에서 같은 부분을 수정한 경우, git이 어느 브랜치의 내용으로 작성해야 하는지 판단하지 못하여 충돌이 발생했을 때 이를 해결하며 병합하는 방법
        * 보통 `같은 파일의 같은 부분`을 수정했을 때 자주 발생

* 연습
  * mkdir git_merge
  * cd git_merge
  * git init
  * touch test.md
  * echo hello > test.md
  * git add .
  * git commit -m 'master 01'
  * echo world > test.md
  * git add .
  * git commit -m 'master 02'
  * echo ssafy > test.md
  * git add .
  * git commit -m 'master 03'
  * git log --oneline
  * git switch -c hotfix
  * git log --oneliine
  * echo fighting >> test.md
  * git add .
  * git commit -m 'hotfix 01'
  * git log --oneline --all --graph
  * git switch master
  * git merge hotfix
  * git log --oneline --all --graph
  * git branch -d hotfix    => `merge 후 브랜치 삭제 !!!!`

  * touch master.md
  * echo master 01 >> master.md
  * git add .
  * git commit -m 'master1'
  * git switch -c hotfix
  * touch hotfix.md
  * echo git >> hotfix.md
  * git add .
  * git commit -m 'hotfix1'
  * echo merge >> hotfix.md
  * git add .
  * git commit -m 'hotfix2'
  * git log --oneline --all --graph
  * git switch master
  * git merge hotfix   => 3-way merge 진행
  * git branch -d hotfix

  * 이 전에 사용했던 git 사용
  * git log --all --oneline --graph
  * git merge login     => 에러 발생 CONFLICT
  * code test.md   => 코드 열어서 수정
    * 꺽새, = 있는 부분 지우고 저장
  * git add .
  * git commit
  * git branch -d hotfix
  * git log --all --oneline --graph

--------
# Git workflow
* branch와 원격 저장소를 이용해 협업을 하는 두 가지 방법

## 원격 저장소 소유권이 있는 경우 => `Shared repository model`
* 원격 저장소가 자신의 소유이거나 Collaborator로 등록되어 있는 경우
* master 브랜치에 직접 개발하는 것이 아니라, 기능별로 브랜치를 따로 만들어 개발
* `Pull Request`를 사용하여 팀원 간 변경 내용에 대한 소통 진행
* 순서
    1. 소유권이 있는 원격 저장소를 로컬 저장소로 `clone` 받기
    2. 사용자는 자신이 작업할 기능에 대한 `브랜치를 생성`하고, 그 안에서 `기능 구현`
    3. 기능 구현이 완료되면, `원격 저장소(본인 브랜치)에` 해당 브랜치를 `push`
    4. 원격 저장소에 각 기능의 브랜치가 반영됨
    5. `Pull Request`를 통해 브랜치를 master에 반영해달라는 요청을 보냄
    6. `병합이 완료된 브랜치는` 불필요하므로 `원격 저장소에서 삭제`
    7. 원격 저장소에서 병합이 완료되면, 사용자는 로컬에서 `master 브랜치로 switch`
    8. 병합으로 인해 변경된 원격 저장소의 `master 내용을 로컬에 Pull`
    9. 원격 저장소 master의 내용을 받았으므로, `기존 로컬 브랜치 삭제` (한 사이클 종료)
    10. 새 기능 추가를 위해, 새로운 브랜치를 생성하며 과정 반복

## 원격 저장소 소유권이 없는 경우 => `Fork & Pull model`
* 오픈소스 프로젝트와 같이, 자신의 소유가 아닌 원격 저장소인 경우
* 원본 원격 저장소를 그대로 내 원격 저장소에 복제 (`Fork`)
* 기능 완성 후 복제한 내 원격 저장소에 Push
* 이후 `Pull Request`를 통해 원본 원격 저장소에 반영될 수 있도록 요청